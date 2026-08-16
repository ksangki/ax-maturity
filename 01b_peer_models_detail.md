# 대표 경쟁 모델 정밀 분석 — AXMM 명세 수준

- 작성: 2026-08-14
- 상위 문서: `01_reference_models.md` (6개 모델 지형도)
- 용도: 책 **2장** "이미 나와 있는 자들, 그리고 그들이 비워둔 자리"의 원재료 / AXMM 설계 검증
- 출처 표기: **[1차]** 원문·보도자료 직접 확인 / **[2차]** 해설 경유 / **[미확인]** 확보 실패

> **왜 이 둘인가**
> - **CMU SEI × Accenture** — CMMI를 만든 조직이 낸 AI판. **구조적으로 가장 가까운 경쟁자**이자 AXMM의 정당화 근거.
> - **MIT CISR** — **실증 데이터가 가장 강하다.** 단계별 기업 분포와 재무성과 상관을 제시하는 유일한 모델.
>
> Cisco AI Readiness Index는 *제품* 관점의 벤치마크(유일한 무료 셀프 진단)라 성격이 달라 `01_reference_models.md` §5에서 별도로 다룬다.

---

# 모델 A. CMU SEI × Accenture — AI Adoption Maturity Model v1.0

## A-1. 기본 정보

| 항목 | 내용 |
|---|---|
| 발표 | **2026년 6월 30일** [1차] |
| 개발 | Carnegie Mellon University SEI × Accenture |
| 저자 | Ipek Ozkaya, Anita Carleton, Sebastián Echeverría, Robert Edman, John Haller, Erin Harper, Michael D. Konrad, Carol J. Smith, Shawn Wray [1차] |
| 구조 | 5레벨 × 8차원 |
| 접근 | **SEI Digital Library에서 다운로드** [1차] · 가격 정보 없음 |
| 계보 | SEI의 40년 성숙도 모델링 자산 (= CMMI 계보) [1차] |

## A-2. 개발 방법론 — 규모로 압도한다

이 모델의 가장 강한 방어선은 내용이 아니라 **개발 규모**다. AXMM이 정면으로 겨룰 수 없는 부분이므로 정직하게 인정하고 다른 축에서 싸운다.

| 방법 | 규모 [1차] |
|---|---|
| 기존 AI 성숙도 시도 리뷰 | **100건 이상** |
| 그중 정밀 분석한 모델 | **36개 이상** |
| 임원 인터뷰 | 20~25명 |
| 실무자 설문 | **약 600명** |
| 파일럿 | Fortune 500 복수 기업 |

> Accenture 최고전략책임자 Manish Sharma의 발언 [2차]:
> *"우리가 SEI와 만든 것은 근본적으로 다르다. 수십 년의 성숙도 모델링 규율에 기반하고, Fortune 500과의 실제 파일럿으로 검증됐다."*

## A-3. 5단계 — 정의 원문

| 레벨 | 이름 | 정의 [1차] |
|---|---|---|
| 1 | **Exploratory AI** | 조직이 자신의 맥락·문화·목표 안에서 AI를 배우는 단계 |
| 2 | **Implemented AI** | 모범이 되는 AI 시스템이 긍정적 영향의 가능성을 보여주는 단계 |
| 3 | **Aligned AI** | 통합되고 일관되게 관리되는 AI가 **측정 가능한 ROI**를 내는 단계 |
| 4 | **Scaled AI** | 전사 AI가 **예측 가능하게** 작동하며 성공이 반복되는 단계 |
| 5 | **Future-Ready AI** | 일관되게 **복제 가능한** AI 활동이 지속적 혁신을 견인하는 단계 |

**읽어야 할 대목:** 3단계의 분수령이 **ROI 측정**이고, 4단계가 **예측 가능성**, 5단계가 **복제 가능성**이다. 전형적인 CMMI 문법 — 정의(Defined) → 정량 관리(Quantitatively Managed) → 최적화(Optimizing)의 번역판이다.

## A-4. 8차원

| 군 | 차원 [1차] | 무엇을 보는가 |
|---|---|---|
| 조직 변화 | **Organizational Strategy** | AI 전략과 사업 목표의 정렬 |
| 조직 변화 | **Workforce and Culture** | 인력 역량과 문화 |
| 조직 변화 | **Workflow Re-engineering** | 업무 흐름 재설계 |
| 조직 변화 | **Risk and Governance** | 위험 관리와 거버넌스 |
| 엔지니어링 | **Data** | 데이터 준비도·품질·거버넌스 |
| 엔지니어링 | **Engineering** | AI 시스템 개발 역량 |
| 엔지니어링 | **Operations** | 운영·모니터링 |
| 엔지니어링 | **Ecosystem** | 기술 생태계·파트너·플랫폼 |

## A-5. 구조와 평가 방식 — **원문 확인 완료 (2026-08-14)**

> 원문 PDF 124쪽을 직접 확인했다. 아래는 전부 **[1차]**다.
> 출처: `sei.cmu.edu/documents/6534/The_AI_Adoption_Maturity_Model.pdf`

### 구조 — 4단 계층

```
차원(Dimension) 8개
  └ 역량영역(Capability Area) 27개  ← 각각 특정 성숙도 레벨에 앵커됨
      └ 목표(Goal)
          └ 실천(Practice)
      └ 예시 산출물(Example Artifacts)
```

각 역량영역 말미에는 이런 문장이 붙는다 — *"Test and Evaluation 역량영역의 모든 목표와 해당 실천이 달성되어야 이 차원이 **Implemented AI 레벨(Level 2)**에 도달한다."*

### ★ 하이브리드 확정 — AXMM의 "우리만 하이브리드" 주장은 성립하지 않는다

원문 §4.3의 문장이 결정적이다.

> *"이 모델은 **성숙도 레벨로도, 차원으로도, 역량영역으로도** 탐색할 수 있다. 조직은 목표 성숙도 수준을 정하고, 현재 역량을 평가하고, 관련 실천과 산출물을 탐색하고, 차원 간 의존성을 이해하는 데 이 모델을 쓸 수 있다."*

그리고 차원마다 **차원별 평가 프로파일 그림**(Figure 5~11, "Example Assessment Outcome for the X Dimension")이 실려 있다. 각 역량영역이 성숙도 레벨에 대해 평가된 결과를 방사형으로 보여준다.

**즉 SEI도 staged + continuous 하이브리드다.** CMMI v2.0의 구조를 그대로 계승했다. Verdict 보도가 옳았고, "5레벨 모델"이라는 다른 보도들은 요약이었다. **AXMM은 이 점에서 독창적이지 않다. 책에서 그렇게 쓰지 않는다.**

### 평가 방식 — 공식 심사 방법론은 없다

SCAMPI에 해당하는 심사 방법론이 **문서에 없다.** 조직이 스스로 목표를 정하고 현재를 평가하는 유연한 구조로 서술돼 있다.

> **따라서 "심사가 아니라 셀프 점검"이라는 AXMM의 차별점도 약해진다.** SEI도 심사를 강제하지 않는다.
>
> **대신 실질적 차별점은 규모다.** 124쪽 · 8차원 · 27역량영역 · 수백 개 실천 항목을 팀장 혼자 오후에 돌릴 수는 없다. 차별점을 *"심사 유무"*가 아니라 **"혼자 15분에 끝낼 수 있는가"**로 다시 잡는다. 30문항이라는 설계가 여기서 값을 한다.

### 역량영역 27개의 레벨 분포 — 이것이 진짜 발견이다

| 앵커된 성숙도 레벨 | 역량영역 수 |
|---|---|
| Level 1 Exploratory | 2 |
| **Level 2 Implemented** | **11** |
| **Level 3 Aligned** | **8** |
| Level 4 Scaled | **1** |
| Level 5 Future Ready | **1** |

**무게중심이 Level 2~3에 쏠려 있고 상위 두 레벨에는 각각 하나뿐이다.** 이 분포가 SEI의 세계관을 드러낸다 — *기초 역량을 모두 갖추면 확장과 미래대비로는 자연히 간다*는 구조다. AXMM은 정반대로 본다. *기초를 갖춘 다음이 진짜 문제다.*

## A-6. 핵심 철학 — AXMM과 수렴하는 지점

> *"진짜 AI 성숙도는 조직이 얼마나 많은 AI를 배포했느냐가 아니라, **신뢰할 수 있고 회복력 있는 역량**, 엄정한 엔지니어링 실천, 그리고 사업 성과에 정렬된 거버넌스를 만들어낼 능력으로 측정된다."* [1차]

**이 문장은 AXMM의 주장과 거의 같다.** "얼마나 깔았나가 아니라 신뢰할 수 있게 만들 능력" = AXMM의 **"생산이 아니라 검증"**.

> **책에서의 처리 원칙:** 숨기지 않는다. **"CMMI를 만든 조직도 같은 결론에 도달했다"**는 교차검증으로 쓴다. 우리 주장은 "우리가 처음"이 아니라 **"기존은 심사·컨설팅용, AXMM은 셀프 점검용"**이다.

---

# 모델 B. MIT CISR — Enterprise AI Maturity (4단계)

## B-1. 기본 정보

| 항목 | 내용 |
|---|---|
| 발표 | 2024-12 초판, 2025 별도 표본 후속 조사 [1차] |
| 저자 | Peter Weill, Stephanie L. Woerner, Ina M. Sebastian [1차] |
| 근거 | **2022년 721개 기업 서베이** + 2024년 9개 기업 임원 16명 인터뷰 [1차] |
| 구조 | 4단계 (차원 축 없이 역량 기반) |
| 접근 | 공식 브리핑 본문·단계표·판정 구간 공개 [1차] / 독립 셀프 진단 없음 |

## B-2. 4단계 — 분포와 재무성과

**이 모델의 압도적 강점: 단계별 기업 분포와 재무성과 상관을 함께 제시한다.** [1차]

| 단계 | 이름 | 비중 | 재무성과 |
|---|---|---|---|
| 1 | Experiment and Prepare | **28%** | 업계 평균 **이하** |
| 2 | Build Pilots and Capabilities | **34%** | 업계 평균 **이하** |
| 3 | Develop AI Ways of Working | **31%** | 업계 평균 **상회** |
| 4 | AI Future-Ready | **7%** | 업계 평균 **상회** |

> **책의 핵심 무기 두 개가 여기서 나온다.**
> 1. **62%가 하위 2단계에 있다.** → *"당신 조직이 아직 실험 단계 같다면, 뒤처진 게 아니라 다수다."* 독자의 방어를 낮추고 진단으로 유도하는 문장.
> 2. **2단계와 3단계 사이에 재무성과의 선이 그어진다.** → 성숙도가 정서적 위안이 아니라 **돈의 문제**임을 보이는 유일한 실증.

## B-3. 단계별 필요 역량 — 상세

### 1단계. Experiment and Prepare (28%)
조직이 인력 교육, AI 정책 수립, 증거 기반 의사결정으로의 전환에 집중하며 자동화된 의사결정 기술을 실험하는 단계.

**필요 역량** [1차]
- 리더십·이사회를 포함한 **AI 리터러시 프로그램**
- 전사 스킬 빌딩
- AI로 가치를 만들 기회의 식별
- **윤리적으로 허용 가능한 사용 범위와 인간 감독 요건의 결정**

### 2단계. Build Pilots and Capabilities (34%)
실험에서 체계적 혁신으로 넘어가는 단계. 기업과 구성원 모두에게 이익이 되는 파일럿을 돌린다.

**필요 역량** [1차]
- **AI 활동의 중요 지표 정의**
- 업무 프로세스의 단순화·자동화
- **조직 내 데이터 사일로 통합**
- AI 사용을 위한 안전한 데이터 준비
- 파일럿에서 얻은 교훈의 **스토리텔링 체계** 구축

**이 단계의 도전** [1차]
> **"command-and-control"에서 "coach-and-communicate"로의 문화 전환.** 현장의 의사결정을 가능하게 하려면 통제형 문화를 코칭형으로 바꿔야 한다.

### 3단계. Develop AI Ways of Working (31%)
AI를 산업화하는 단계. 재무성과가 업계 평균을 넘어서기 시작하는 분수령.

**필요 역량** [1차]
- **확장 가능한 전사 아키텍처**
- 데이터와 성과를 투명하게 보여주는 **비즈니스 대시보드**
- **test-and-learn 문화**
- 업무 프로세스 자동화의 확대
- 파운데이션 모델과 sLM(소형 언어 모델) 활용
- **자체 모델(proprietary model) 개발**

**이 단계의 도전** [1차]
> **AI를 적용하기 전에 복잡한 프로세스를 먼저 단순화하는 것.** 그리고 "아키텍처, 재사용, 에이전트"의 확보.

### 4단계. AI Future-Ready (7%)
AI가 **모든 의사결정에 내장된** 단계. 자체 AI 역량을 내부에 쓸 뿐 아니라 그것에 기반한 **새로운 서비스를 외부에 판다.**

**필요 역량** [1차]
- **human-in-the-loop의 최적 요건 결정**
- AI 기반 서비스의 상용화

---

# C. AXMM과의 정밀 대조

## C-1. 레벨 매핑

| AXMM | SEI×Accenture | MIT CISR | 분수령의 차이 |
|---|---|---|---|
| **L1 각자도생** | 1 Exploratory | 1 Experiment and Prepare | 대체로 일치 |
| **L2 반복** | 2 Implemented | 2 Build Pilots | 대체로 일치 |
| **L3 레일** | 3 Aligned | 3 Develop AI Ways of Working | SEI·MIT는 **ROI/산업화**, AXMM은 **표준과 권장 경로** |
| **L4 검증** | 4 Scaled | — | ★ **여기서 갈린다.** 그들은 *확장*, 우리는 *검증* |
| **L5 진화** | 5 Future-Ready | 4 AI Future-Ready | 그들은 *복제 가능성*, 우리는 *되돌아옴* |

### ★ 결정적 차이 — 4단계에 무엇을 놓는가

**SEI는 4단계를 `Scaled`(전사 확장, 예측 가능한 작동)로 놓는다. AXMM은 `검증`으로 놓는다.**

이 차이가 두 모델의 세계관 차이 전부다.

- **SEI의 전제:** 확장이 어렵다. 전사로 퍼뜨리고 예측 가능하게 만드는 것이 성숙의 관문이다.
- **AXMM의 전제:** AI 시대에 **확장은 쉽다.** 도구가 그걸 대신해준다. 어렵고 병목인 것은 **만든 것이 맞는지 확인하는 일**이다.

AXMM의 근거는 이론이 아니라 실제 진단이다. 어느 조직의 라이프사이클 진단에서 **평가·측정·개선 축이 통째로 비어 있었고**, 품질 평가 항목의 소견은 이랬다 — *"에이전트가 제대로 동작하는지 평가하는 도구가 없다. 사람이 일일이 할 수 없으니 평가용 에이전트를 만들어야 한다."* 투입(토큰·비용)은 재고 있는데 **산출 지표가 없어 되돌릴 수가 없는** 상태였다.

> **원문 확인 결과:** SEI에는 `Engineering` 차원의 `Test and Evaluation` 역량영역이 있고 2단계에 귀속된다. AXMM과의 차이는 검증의 존재가 아니라 **2단계 기초 요건으로 놓느냐, 4단계 분수령으로 놓느냐**다.

### ★ 5단계의 차이 — 도달인가, 되돌아옴인가

| 모델 | 최고 단계의 정의 |
|---|---|
| SEI | **복제 가능성** — 일관되게 복제 가능한 활동이 혁신을 견인 |
| MIT | **편재성** — AI가 모든 의사결정에 내장, 외부 판매까지 |
| **AXMM** | **되돌아옴** — 결과가 개선과 보상으로 되돌아와 다음 바퀴를 돌림 |

AXMM의 근거: Gartner 실증에서 **고성숙 조직조차 45%만** AI 프로젝트를 3년 이상 유지했고, Cisco의 최상위 조직 비율은 **3년째 13%로 고정**이다. 도달한 조직도 미끄러진다. **성숙은 정상에 서는 게 아니라 미끄러지지 않는 능력이다.**

## C-2. 차원 매핑

| AXMM 6축 | SEI 8차원 | MIT (역량 기반) |
|---|---|---|
| **A 인식·동기·역량** | Workforce and Culture | 1단계 AI 리터러시, 스킬 빌딩 |
| **B 기획·개발** | Workflow Re-engineering, Engineering | 2단계 지표 정의·프로세스 단순화 |
| **C 연동·배포·운영** | Operations, Ecosystem | 3단계 확장 아키텍처·재사용 |
| **D 평가·측정·개선** ★ | *(Risk and Governance에 일부 흡수 추정)* | 3단계 대시보드·test-and-learn |
| **I 자원·비용** | *(대응 없음)* | *(대응 없음)* |
| **J 보안·거버넌스** | Risk and Governance | 1단계 윤리·인간 감독 |
| *(AXMM이 의도적으로 제외)* | **Data**, **Organizational Strategy** | 2단계 데이터 사일로 통합 |

**두 가지가 눈에 띈다.**

1. **`I 자원·비용`에 대응하는 차원이 어느 모델에도 없다.** 예산·토큰·컴퓨팅을 어떻게 확보하고 배분하는가는 글로벌 대기업 모델의 관심사가 아니다. **한국 조직의 팀장에게는 가장 먼저 막히는 벽인데도.** AXMM 고유 기여 중 하나.
2. **AXMM은 `Data`와 `Organizational Strategy`를 뺐다.** 의도적이다. 1차 독자인 팀장의 권한 밖이고, 물어봐야 무력감만 남는다. 대신 결과 리포트에서 "전제 조건"으로 안내한다.

## C-3. 성격 대조 — 한 장으로

| | SEI×Accenture | MIT CISR | **AXMM** |
|---|---|---|---|
| 레벨 | 5 | 4 | 5 |
| 차원 | 8 | 없음(역량 기반) | 6 |
| 문항 수 | 미확인 | 미공개 | **30** |
| 평가 주체 | 미확인(도구 동반) | 미공개 | **셀프 전용** |
| 접근성 | 다운로드 | **공식 브리핑 공개·독립 셀프 진단 없음** | **무료 웹 · 15분** |
| 표본 | Fortune 500 | 721개 기업 | 한국 조직 현실 |
| 대상 | CxO | CxO | **AX 추진 담당자·팀장** |
| 4단계 | 확장 | *(3단계 산업화)* | **검증** ★ |
| 5단계 | 복제 가능성 | 편재성 | **되돌아옴** ★ |
| 산출 | 로드맵 | 벤치마크 | **다음 한 걸음** |
| 응답 척도 | 미확인 | 미공개 | **보유/보완/신규** |
| 게임화 방지 | 없음 | 해당 없음 | **인증·배지·순위표 없음** ★ |

---

# D. 미확인 항목과 확인 계획

책에 쓰기 전에 반드시 정리해야 할 것들. **확인 못 하면 "보도에 따르면"으로 처리하고 단정하지 않는다.**

| # | 미확인 항목 | 왜 중요한가 | 확인 방법 |
|---|---|---|---|
| 1 | SEI 모델의 **평가 방식** (자가 vs 심사) | AXMM의 핵심 차별점("심사가 아니라 셀프")이 여기에 걸려 있다 | SEI Digital Library PDF 다운로드 |
| 2 | SEI가 **5레벨인가 차원별 연속 등급인가** | 보도가 엇갈린다. 후자면 AXMM 하이브리드와 같은 계열 | 동일 |
| 3 | SEI 8차원의 **레벨별 practice 목록** | AXMM 30문항과 정밀 매핑해 겹침을 정직하게 표기해야 함 | 동일 |
| 4 | SEI에 **검증(verification)이 독립 practice로 있는가** | AXMM의 최대 독창성 주장이 걸려 있다 | 동일 |
| 5 | MIT CISR **4단계 판정 기준** | **해결:** 총 AI 효과성 0~49 / 50~74 / 75~99 / 100점 | 2024 공식 브리핑 직접 확인 |
| 6 | SEI 모델 **접근 비용** | "무료 웹" 차별점의 강도가 달라진다 | 다운로드 페이지 확인 |

> **①~④·⑥은 SEI PDF 한 건으로 모두 해결된다.** 2장 집필 전 최우선 확보 대상.

---

## 참고문헌

- CMU SEI, *The AI Adoption Maturity Model v1.0* (2026-06-30) — https://www.sei.cmu.edu/library/ai-adoption-maturity-model/
- SEI 보도자료 — https://www.sei.cmu.edu/news/sei-and-accenture-release-ai-adoption-maturity-model-to-help-organizations-scale-ai-with-predictable-outcomes/
- Accenture 뉴스룸 (2026) — https://newsroom.accenture.com/news/2026/accenture-and-the-carnegie-mellon-university-software-engineering-institute-launch-ai-adoption-maturity-model-to-help-organizations-scale-ai-with-predictable-outcomes
- Verdict, *Accenture and CMU SEI introduce AI Adoption Maturity Model* — https://www.verdict.co.uk/accenture-cmu-ai-adoption-model/
- MIT Sloan, *What's your company's AI maturity level?* — https://mitsloan.mit.edu/ideas-made-to-matter/whats-your-companys-ai-maturity-level
- MIT CISR, *Building Enterprise AI Maturity* — https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian
- MIT CISR, *Grow Enterprise AI Maturity for Bottom-Line Impact* — https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer
- VKTR, *MIT's 4 Stages of Enterprise AI Maturity* — https://www.vktr.com/ai-technology/mits-4-stages-of-enterprise-ai-maturity/
