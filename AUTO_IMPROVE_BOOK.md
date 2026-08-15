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

4장은 `축을 왜 조직 기능이 아니라 구성원의 여정으로 잡았는가`라는 책의 설계 판단이 가장 선명하게 드러나는 장이다. 저자 목소리, 추상성, 중복, 독자 효용을 동시에 시험하기 좋아 첫 대상으로 삼는다.

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

## 파일럿 이후

4장의 diff가 실제로 낫다고 판단될 때만 다른 장으로 확장한다. 권장 순서는 다음과 같다.

1. 4장 — 축을 여정으로 잡은 설계 판단
2. 10장 — `만든 다음`의 병목과 조직 역할
3. 12장 — 자원·비용 축
4. 들어가며/도입부 — 마지막에만 적용. 개인 목소리가 가장 강해 자동 최적화에 가장 민감하다.

전권을 한 번에 하나의 artifact로 돌리지 않는다. 전권 중복은 `DEDUP_DECISIONS.md`가 관리하고, auto-improve는 장 내부의 작은 품질 개선에 집중시킨다.
