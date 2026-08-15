# AX 책 Auto-Improve 운영 가이드

목적은 원고를 자동 재작성하는 것이 아니다. 현재 원고에서 작은 개선 후보를 만들고, 책 전용 rubric과 독립 evaluator의 pairwise gate를 통과한 변경만 남긴다.

## 왜 별도 패치가 필요한가

`crimeacs/auto-improve` 기본 구현은 일반 텍스트 artifact를 대상으로 하며 평가·mutation·pairwise prompt에서 artifact 앞부분을 6,000~12,000자 정도만 사용한다. 이 책의 장별 원고는 대체로 그보다 길다.

`scripts/patch_auto_improve_for_book.py`는 upstream 파일을 직접 수정하지 않고 임시 runtime 사본을 만든 뒤 다음만 바꾼다.

1. artifact prompt 범위를 기본 24,000자로 늘린다.
2. rubric prompt 범위를 기본 8,000자로 늘린다.
3. numeric rubric scoring도 `IMPROVE_EVALUATOR`를 사용하게 한다.
4. upstream의 surgical diff, best-of-N, 양방향 pairwise keep/discard 구조는 그대로 둔다.

## 두 가지 실행 방식

이 저장소에서는 두 방식 모두 사용할 수 있다.

- **GPT 직접 파일럿:** ChatGPT가 장 전체와 rubric을 읽고 mutation 후보 생성 → 별도 평가 패스 → 양방향 pairwise → KEEP/DISCARD를 수행한다. 별도 Gemini API 키가 필요 없다. `results/ch04-gpt56-pilot.md`가 첫 실행 기록이다.
- **upstream 자동 실행:** 아래 래퍼로 `crimeacs/auto-improve`를 직접 실행한다. 이 경우 Gemini API 키가 필요하다.

GPT 직접 방식은 mutator와 evaluator가 완전히 다른 모델은 아니라는 한계가 있으므로, pairwise 순서를 바꿔 두 번 평가하고 최종 diff를 사람이 검토한다.

## upstream 자동 실행 준비

Auto-Improve는 별도 checkout으로 둔다. 현재 확인한 upstream 기준 커밋은 `03aa5a9464b867bd8ce273841b07bcbf6890d7e7`이다.

```bash
git clone https://github.com/crimeacs/auto-improve.git ../auto-improve
cd ../auto-improve
git checkout 03aa5a9464b867bd8ce273841b07bcbf6890d7e7
pip install requests
cd ../ax-maturity
```

Gemini API key를 환경변수에 둔다.

```bash
export GEMINI_API_KEY=...
export AUTO_IMPROVE_HOME=../auto-improve
```

Mutator와 evaluator를 분리하고 싶으면 둘을 각각 지정한다. 지정하지 않으면 upstream 기본값을 따른다.

```bash
export IMPROVE_MUTATOR=...
export IMPROVE_EVALUATOR=...
```

## 첫 파일럿: 4장

4장은 `축을 왜 조직 기능이 아니라 구성원의 여정으로 잡았는가`라는 책의 설계 판단이 가장 선명하게 드러나는 장이다. 저자 목소리, 추상성, 중복, 독자 효용을 동시에 시험하기 좋아 첫 대상으로 삼았다.

GPT-5.6 Sol 직접 파일럿에서는 4회 중 3개를 KEEP하고 1개를 DISCARD했다. 상세 판단은 `results/ch04-gpt56-pilot.md`에 남겼다.

upstream으로 재현하려면 다음처럼 실행한다.

```bash
scripts/run_auto_improve_book.sh chapters/04_draft.md ch04-pilot 4
```

기본값은 후보 3개, 평가 2회, 최대 4 iteration, 목표 92점이다. 처음부터 10 iteration을 돌리지 않는다. 이미 편집을 거친 원고라 과도한 최적화가 오히려 문체를 평평하게 만들 수 있기 때문이다.

## 채택 규칙

결과가 `keep`이어도 바로 본문에 합치지 않는다.

```bash
git diff main...improve/ch04-pilot -- chapters/04_draft.md
```

다음 네 가지를 사람이 마지막으로 본다.

- 원문에 없던 경험이나 사실을 만들어내지 않았는가
- `DEDUP_DECISIONS.md`의 장별 소유권을 깨지 않았는가
- 문장이 더 매끈해진 대신 저자 목소리가 약해지지 않았는가
- 수정 이유를 한 문장으로 설명할 수 있는가

하나라도 애매하면 원문을 유지한다.

## 전권 적용 결과

4장 파일럿이 유효해 같은 원칙으로 들어가며·도입부·1~15장·에필로그·부록 A~C를 전부 검토했다.

- 4장 파일럿: **3건 KEEP**
- 전권 본 패스: **180건 적용**
- 5장 최종 논리 일관성 보정: **5건 적용**
- 총 품질 수정: **188건**

큰 재작성은 하지 않았다. 실제로 효과가 컸던 것은 `AI 같은 문장` 자체를 찾는 것보다 다음 유형을 잡는 일이었다.

1. 외부 수치에서 원인·승강·행동을 근거 없이 추론한 문장
2. 앞뒤 절 또는 다른 장의 규칙과 충돌하는 단정
3. `대개`, `반드시`, `유일`, 임의의 기간·횟수처럼 근거보다 강한 표현
4. `보완 = 안 정해짐`처럼 모델의 실제 정의보다 좁게 해석한 방법론
5. 뒤에서 설명할 내용을 미리 결론내는 메타 문장과 중복

상세 반영 목록은 `results/full-book-gpt56-pass.md`에 있다. 전권 적용 후 `04_manuscript.md`와 `docs/index.html`을 다시 생성했고, 사이트 구조 검증과 `git diff --check`를 통과했다.

## 이후 운영

전권을 한 번에 하나의 artifact로 돌리지 않는다. 전권 중복과 장별 소유권은 `DEDUP_DECISIONS.md`가 관리하고, auto-improve는 장 내부의 작은 품질 개선에 집중시킨다.

특히 들어가며·도입부처럼 개인 목소리가 강한 부분은 자동 점수보다 원문 보존을 우선한다. 이미 좋은 문장은 더 매끈하게 만들 수 있다는 이유만으로 바꾸지 않는다.
