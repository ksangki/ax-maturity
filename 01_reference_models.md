# 기존 AI/AX 성숙도 모델 딥리서치 — 지형도와 빈틈

- 작성: 2026-08-14 · 공식 자료 재확인: 2026-08-16
- 목적: ① 경쟁 지형 파악 ② 책 PART 1의 이론 좌표 ③ 우리 모델의 설계 요구사항 도출
- 출처 신뢰도 표기: **[1차]** 원문·공식 브리핑 직접 확인 / **[2차]** 유료·비공개 세부를 보도·해설로만 확인

> **2026-08-16 재확인:** SEI 원문 PDF와 MIT CISR 2024·2025 공식 브리핑 본문은 공개돼 있다. MIT의 단계 산식·분포·재무성과와 후속 조사까지 [1차]로 올린다. Gartner는 일곱 기둥과 공개 조사 결과만 [1차]이며, 유료 툴킷의 세부 판정 지침과 중간 단계 설명은 확인 범위 밖이다.

---

## 0. 한눈에 보는 지형도

| 모델 | 발표 | 레벨 | 차원(축) | 성격 | 접근성 |
|---|---|---|---|---|---|
| **CMMI** (조상) | 1991~ / v2.0 2018 | 5 (Initial→Optimizing) | 프로세스 영역 | 처방+심사 | 유료 심사(SCAMPI) |
| **CMU SEI × Accenture — AI Adoption Maturity Model v1.0** | **2026-06-30** | 5 (Exploratory→Future-Ready) | **8** (조직변화 4 + 엔지니어링 4) | 처방+로드맵 | PDF 공개 / 심사는 별도 |
| **MIT CISR — Enterprise AI Maturity** | 2024-12, 2025 후속 조사 | 4 (Experiment→Future Ready) | 효과성 점수 기반 | 서술+실증 | 공식 브리핑 공개 / 독립 셀프 진단 없음 |
| **Gartner — AI Maturity Model** | 2024-11 | 5수준 | 7 (전략·유스케이스·제품·거버넌스·엔지니어링·데이터·생태계·운영모델·사람문화) | 서술+툴킷 | 세부 툴킷 유료 |
| **Cisco — AI Readiness Index** | 2023~2025 연례 | 4구간(Pacesetter 등) | 6 (전략·인프라·데이터·인재·거버넌스·문화) | 벤치마크 서베이 | **무료 셀프 진단 있음** |
| **학술 AIMM 다수** | 2015~ | 4~9 (5가 최빈) | 데이터·기술·자동화·거버넌스·사람·조직 | 대부분 **서술** | 논문 |

**한 문장 요약:** 5레벨 구조는 사실상 업계 표준으로 굳었고, 차원 축은 6~8개로 수렴한다. **그런데 거의 전부가 "당신은 몇 단계인지" 말해줄 뿐, "그래서 내일 뭘 만들지"는 말해주지 않는다.** 그리고 대부분이 대기업 임원용이다.

---

## 1. 계보 — 이 모든 것의 조상은 하나다

성숙도 모델의 계보를 짚어야 하는 이유는 단순하다. **지금 쏟아지는 AI 성숙도 모델은 전부 CMMI의 문법을 빌려 쓰고 있다.** 5단계, 레벨별 실천항목, 영역별 평가 — 1991년 CMU SEI가 국방부 납품업체를 걸러내려고 만든 그 구조 그대로다.

- **CMMI (Capability Maturity Model Integration)** — CMU SEI 개발, 현재 ISACA 산하 CMMI Institute 운영. 5단계: Initial → Managed → Defined → Quantitatively Managed → Optimizing. **[1차]** ([Wikipedia](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration))
  - 두 가지 표현법: **staged**(조직 전체 한 등급) vs **continuous**(영역별 등급). v2.0에서 둘을 함께 지원. → *우리 하이브리드 설계의 직접 선례.*
  - 심사: **SCAMPI**. Class A가 공식 등급을 부여하며 미 국방부 조달 요건에 쓰였다. **[1차]** ([SCAMPI](https://en.wikipedia.org/wiki/Standard_CMMI_Appraisal_Method_for_Process_Improvement))
- **TMMi** — 테스트 프로세스판 CMMI. 저자의 직접 실무 영역.

> **저자가 짚어야 할 대목:** CMMI는 "개선 도구"로 태어났지만 현장에서는 **"등급 취득"이 목적이 되는 순간 망가졌다.** 심사를 통과하려고 문서를 만들고, 등급을 딴 뒤 원래대로 돌아가는 일이 흔했다. 10년간 그걸 지켜본 사람이 AX 성숙도 모델을 만든다면, 그 실패를 되풀이하지 않게 설계해야 한다. → **이것이 "심사 없는 셀프 점검"이라는 결정의 진짜 이유다.** 등급을 남에게 증명하는 순간 게임이 시작되기 때문이다.

---

## 2. CMU SEI × Accenture — AI Adoption Maturity Model v1.0

**가장 중요한 경쟁 모델.** CMMI를 만든 바로 그 조직이 낸 AI판이다.

- 발표: **2026년 6월 30일** (불과 6주 전). 저자: Ipek Ozkaya, Anita Carleton, Sebastián Echeverría, Robert Edman, John Haller, Erin Harper, Michael D. Konrad, Carol J. Smith, Shawn Wray **[1차]** ([SEI Library](https://www.sei.cmu.edu/library/ai-adoption-maturity-model/))
- **5레벨:** Exploratory → Implemented → Aligned → Scaled → Future-Ready **[1차]**
- **8차원** **[1차]**
  - 조직 변화 4: Strategy / Workforce / **Workflow re-engineering** / Risk
  - AI 생애주기 엔지니어링 4: Data / Engineering / Operations / Technology ecosystem
- **개발 규모:** 기존 AI 성숙도 시도 **100개 이상** 체계적 리뷰 + 임원 인터뷰 약 25건 + 실무자 설문 약 600명 + Fortune 500 파일럿 **[1차]** ([SEI 보도](https://www.sei.cmu.edu/news/sei-and-accenture-release-ai-adoption-maturity-model-to-help-organizations-scale-ai-with-predictable-outcomes/), [Accenture 뉴스룸](https://newsroom.accenture.com/news/2026/accenture-and-the-carnegie-mellon-university-software-engineering-institute-launch-ai-adoption-maturity-model-to-help-organizations-scale-ai-with-predictable-outcomes))
- **핵심 철학 (원문 인용, [1차]):** *"True AI maturity is not measured by how much AI an organization deploys, but by its ability to build trustworthy and resilient capabilities, rigorous engineering practices, and governance approaches aligned with business outcomes."*

**우리 모델과의 관계 — 정직한 평가:**

이 문장은 우리 책의 주장과 **거의 같다.** "얼마나 많이 깔았나가 아니라 신뢰할 수 있게 만들 능력이 있나" = 저자의 "**생산이 아니라 검증**". 겹친다는 사실을 숨길 이유가 없다. 오히려 **"CMMI를 만든 조직도 같은 결론에 도달했다"는 강력한 교차검증**으로 쓴다.

차별점은 세 가지다:
1. **표본이 Fortune 500이다.** 파일럿 대상이 명시적으로 Fortune 500이다. 8차원 중 Technology ecosystem·Operations는 전담 조직이 있는 규모를 전제한다. 한국의 팀장이 이 자를 그대로 대면 대부분 Level 1이 나오고, 그건 진단이 아니라 좌절이다.
2. **8차원은 셀프 점검에 너무 무겁다.** 차원당 최소 5문항이면 40문항. 응답 이탈이 난다. → 우리는 **6영역 30문항**으로 줄인다.
3. **처방이 로드맵 수준이다.** "assessment-based roadmap"은 방향이지 구현이 아니다. → 저자는 빌더로서 각 단계의 **다음 한 걸음을 구체물로** 준다.

> **행동 항목:** SEI 원문 PDF를 반드시 내려받아 8차원의 레벨별 practice를 확인할 것. 우리 6영역과 매핑표를 만들어 책에 싣는다. 겹치는 부분은 겹친다고 쓰고, 출처를 밝힌다.

---

## 3. MIT CISR — Enterprise AI Maturity (4단계)

가장 **실증 데이터가 강한** 모델. 2022년 721개 기업 서베이 기반이며 공식 브리핑에서 산식과 결과를 직접 확인했다. **[1차]**

| 단계 | 이름 | 비중 | 내용 |
|---|---|---|---|
| 1 | Experiment and Prepare | **28%** | AI 리터러시 교육, 정책 수립, 실험 |
| 2 | Building Pilots and Capabilities | **34%** | 파일럿 배포, 데이터 사일로 통합 |
| 3 | Develop AI Ways of Working | **31%** | 산업화·확장 가능 아키텍처·테스트 학습 문화 |
| 4 | Become AI Future Ready | **7%** | AI가 의사결정 전반에 스며듦 |

**핵심 실증:** 1~2단계 기업은 **업계 평균 이하** 재무성과, 3~4단계는 **업계 평균 상회**. 저자: Peter Weill, Stephanie Woerner, Ina Sebastian **[1차]** ([MIT CISR 2024 공식 브리핑](https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian))

**책에서 쓸 방식:** 이 **62%(1~2단계)**라는 숫자가 우리 책 도입부의 핵심 무기다. *"당신 조직이 아직 실험 단계라고 느낀다면, 그건 뒤처진 게 아니라 다수다."* — 독자의 방어를 낮추고 진단으로 유도하는 문장.

**2025 후속:** 별도 표본 152개 기업의 분포는 13·23·46·18퍼센트였고 2→3단계에서 재무성과가 업계 평균 위로 바뀌는 경계는 유지됐다. 같은 기업을 추적한 패널은 아니다. ([MIT CISR 2025 공식 브리핑](https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer))

**한계:** 브리핑 본문과 판정 구간은 공개됐지만, 입력값을 같은 방식으로 산출할 공개 설문지나 독립 셀프 진단은 없다. 결과를 읽을 수 있는 것과 같은 자로 우리 조직을 재는 것은 다르다.

---

## 4. Gartner — AI Maturity Model (5레벨 · 7기둥)

- **발표:** 2024년 11월 20일. 현재 준비도를 추정해 투자 우선순위와 로드맵을 정하는 모델 **[1차]** ([Gartner 공식 초록](https://www.gartner.com/en/documents/5937907))
- **5수준:** 공개 조사에서는 1수준의 끝점을 `planning/beginning`, 5수준의 끝점을 `leadership`으로 설명한다. 중간 수준의 공식 명칭은 공개 자료에서 확인하지 못했다. **[1차]**
- **7기둥:** AI 전략 / AI 유스케이스·제품 포트폴리오 / AI 거버넌스 / AI 엔지니어링 / AI 데이터 / AI 생태계·운영모델 / 사람·문화 **[1차]**
- **조사:** 고성숙 조직 평균 4.2~4.5점, 저성숙 조직 1.6~2.2점. 2024년 4분기 6개국 응답자 432명의 일곱 문항 자기보고 조사 **[1차]**
- **별도 실증 [1차]:** 고성숙 조직조차 **45%만** AI 프로젝트를 3년 이상 운영 유지 (저성숙은 20%). ([Gartner 보도자료](https://www.gartner.com/en/newsroom/press-releases/2025-06-30-gartner-survey-finds-forty-five-percent-of-organizations-with-high-artificial-intelligence-maturity-keep-artificial-intelligence-projects-operational-for-at-least-three-years))

**책에서 쓸 방식:** 이 45%가 **"성숙 = 도달이 아니라 유지"**라는 우리 L5(진화)의 논거다. 높은 등급을 받은 조직조차 절반 이상이 3년을 못 버틴다. 성숙도는 정상에 도달하는 게 아니라 **미끄러지지 않는 능력**이다.

**한계:** 유료 구독. 툴킷이 있으나 Gartner 고객만 쓴다.

---

## 5. Cisco — AI Readiness Index (유일하게 셀프 진단이 열려 있는 모델)

- **6기둥:** 전략 / 인프라 / 데이터 / 인재 / 거버넌스 / 문화 **[1차]**
- **Pacesetters(최상위) = 전체의 13%.** 3년 연속 동일 비율 **[1차]**
- 격차 데이터 **[1차]** ([Cisco 뉴스룸](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2025/m10/cisco-ai-research-the-most-ai-ready-companies-outpace-peers-in-the-race-to-value.html), [2025 Index PDF](https://www.cisco.com/c/dam/m/en_us/solutions/ai/readiness-index/2025-m10/documents/cisco-ai-readiness-index-2025-realizing-the-value-of-ai.pdf))
  - 명확한 AI 전략 보유: Pacesetter **99%** vs 전체 58%
  - 필요한 속도·규모로 배포: **97%** vs 41%
  - 직원 AI 숙련도 확보: **75%** vs 16%
  - **에이전트 행동을 가드레일과 실시간 모니터링으로 통제 가능: 84% vs 24%** ← *저자의 "레일" 명제를 정면으로 뒷받침하는 최고의 외부 수치*

**주목:** Cisco는 **무료 셀프 진단 도구**([Look-up Tool](https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index/lookup-tool.html))를 운영한다. **우리 사이트의 가장 가까운 벤치마크다.** 다만 성격이 다르다 — Cisco는 *벤치마크 서베이*(남과 비교)이고, 우리는 *처방 도구*(다음 한 걸음)다. Phase 2에서 UX를 반드시 살펴볼 것.

> **13%가 3년째 고정**이라는 사실도 중요하다. 도구는 좋아지는데 성숙한 조직 비율은 늘지 않는다. → **"도구를 깐다고 성숙해지지 않는다"**는 우리 명제의 실증.

---

## 6. 학계 — 무엇이 이미 밝혀졌나

### 6-1. AI 성숙도 모델 체계적 문헌고찰 (Sadiq et al., 2021) **[1차]**
([PMC8409328](https://pmc.ncbi.nlm.nih.gov/articles/PMC8409328/))

2015~2020년 15개 주요 논문 분석. 우리 설계에 직접 쓸 결론들:

- **레벨 수:** 4~9개로 분포하나 **5레벨이 최빈**이자 권장. *"5레벨이 세부의 분산을 막는 데 적합하다."* → **우리의 5레벨 결정에 학술 근거 확보.**
- **공통 차원:** 데이터·분석 / 기술·도구 / 지능형 자동화 / **거버넌스** / **사람** / **조직** (13개 연구에서 반복)
- **용어 혼란:** dimension, construct, element, indicator, process area — *"표준 용어가 없다."* → 우리는 **"영역(Practice Area)"**으로 통일하고 그 이유를 밝힌다(CMMI 계보 계승).
- **결정적 빈틈 3가지:**
  1. **처방 부족** — 15편 중 **서술 13편**, 처방 6편, 비교 3편. *"개선 로드맵을 제시하는 처방적 모델이 여전히 과소 대표된다."*
  2. **검증 부족** — **47%만** 모델을 검증했다.
  3. **적용 사례 전무** — *"기존 AIMM을 실제로 적용한 연구가 없다."*
  4. **이론적 빈약** — *"성숙 개념에 대한 이론적 성찰이 대체로 빠져 있다."*

> **이 네 가지가 그대로 우리의 설계 요구사항이 된다.** 특히 ③ "아무도 실제로 안 써봤다" — 우리는 사이트로 **실제 응답을 받아본 뒤 책을 쓴다.** 이게 저자가 정한 진행 순서(모델→사이트→책)의 학술적 정당화다.

### 6-2. 성숙도 모델 자체에 대한 비판 **[2차]**

성숙도 모델은 오래전부터 비판받아 왔고, 저자는 이걸 **회피하지 말고 책 앞부분에서 정면으로 다뤄야 한다.** 그래야 10년 경력자가 쓰는 책이 된다.

- **Pöppelbuß & Röglinger (ECIS 2011)** — *"성숙도 모델은 널리 쓰이지만 개념 자체가 자주 비판받는다"*며 설계 원칙 프레임워크를 제시. ([AIS eLibrary](https://aisel.aisnet.org/ecis2011/28/))
- **비즈니스 프로세스 성숙도 모델 문헌고찰 (2024)** — *"이론적 기반이 빈약하고, 모델이 너무 많아 실무자가 고르질 못한다. 바람직한 성숙 수준을 식별하거나 개선을 실행하는 데 주는 지침이 제한적이며, 처방적 사용을 위한 설계 원칙은 거의 충족되지 않는다."* ([Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/10580530.2024.2332210))
- **Mettler (2011)** — 성숙도 평가 모델의 설계과학 접근. ([참조](https://scispace.com/papers/maturity-assessment-models-a-design-science-research-3bc05eg42j))

**주요 비판 요지 4가지와 우리의 대응:**

| 비판 | 우리 모델의 대응 |
|---|---|
| ① **단계론적 단순화** — 현실은 계단이 아닌데 계단으로 그린다 | 전체 등급 + **영역별 등급**을 함께 보여 "우리는 3단계"라는 납작한 결론을 막는다 |
| ② **이론 부재** — 왜 그 순서인지 근거가 없다 | 순서의 근거를 **J-curve 여정 + 3대 부채 청구 시점**이라는 인과로 설명한다 |
| ③ **등급이 목적이 되는 게임화** | **심사·인증을 아예 만들지 않는다.** 증거 기입을 강제하고 결과를 남에게 증명하는 용도로 쓰지 않는다 |
| ④ **처방 부재** — 진단만 하고 끝 | **레벨별 "다음 한 걸음"을 구체물로** 제시. 이게 책의 본체다 |

---

## 7. 횡단 분석 — 여섯 모델이 합의한 것과 갈라지는 것

**합의한 것 (안전하게 따라도 되는 것):**
1. **5레벨 구조** (MIT만 4)
2. **차원 축의 존재** — 6~8개
3. 공통으로 등장하는 축: **전략 / 데이터·기술 / 거버넌스 / 사람 / 문화 / 운영**
4. **대다수 조직이 하위 단계에 정체** — MIT 62%, Gartner "대다수 L1~2", Cisco Pacesetter 13%
5. **상위 단계가 재무성과와 상관** — MIT가 가장 강한 증거

**갈라지는 것 (우리가 선택해야 하는 것):**
| 쟁점 | 진영 A | 진영 B | **우리 선택** |
|---|---|---|---|
| 표현법 | staged(전체 한 등급) | continuous(영역별) | **하이브리드 — 둘 다** |
| 평가 주체 | 심사·컨설팅 (SEI·MIT·Gartner) | 셀프 (Cisco) | **셀프 전용** |
| 초점 | 기술·인프라 준비도 | 일·조직 재설계 | **일·조직 + 검증** |
| 용도 | 벤치마크(남과 비교) | 개선(내가 나아짐) | **개선 처방** |

**아무도 제대로 안 한 것 (= 우리의 자리):**
- **검증(verification)을 독립 축으로 세운 모델이 없다.** 거버넌스·리스크는 있는데, "AI가 만든 것이 맞는지 확인하는 능력"을 별도 역량으로 계량하는 모델이 없다. **AI 시대 성숙도의 병목은 생산이 아니라 검증인데도.** ← *이게 우리 모델의 가장 독창적인 기여다.*
- **인지부채·의도부채를 다루는 모델이 없다.** 기술부채는 엔지니어링 축에 흡수되지만, "아무도 전체를 모름"과 "왜 만들었는지 사라짐"은 어떤 모델에도 없다.
- **중간 리더용 모델이 없다.** 전부 CxO 대상이다.

---

## 8. 결론 — 우리 모델의 설계 요구사항 (Phase 1 확정 입력)

위 리서치에서 도출된 구속 조건:

1. **5레벨 유지** — 학술 권장이자 업계 표준. 굳이 다르게 갈 이유 없음. 대신 **레벨 이름을 한국어 현장 언어로** 지어 차별화한다.
2. **6영역** — 8은 셀프 점검에 무겁고 4는 성기다. **검증을 독립 영역으로 반드시 세운다.**
3. **하이브리드 표현** — 전체 1개 등급 + 영역별 6개 등급. CMMI v2.0의 선례가 있다.
4. **심사 없음, 인증 없음** — 게임화 방지. 대신 **증거 기입 필수**로 자기기만을 막는다.
5. **최저 영역이 전체 등급을 결정**(weakest-link) — CMMI staged 원칙 계승. "가장 약한 고리가 조직의 실제 수준"
6. **처방이 본체** — 학술이 지목한 최대 빈틈. 각 레벨·영역마다 "다음 한 걸음"을 구체물로.
7. **문항 30개 이내** — 응답 이탈 방지. 6영역 × 5레벨 = 30.
8. **실제 응답을 받아본 뒤 책을 쓴다** — "아무도 적용해본 적 없다"는 학술 빈틈을 우리가 메운다.
9. **기존 모델을 정직하게 인용한다** — 특히 SEI 모델. "내가 처음"이라고 하지 않는다. 우리 주장은 *"기존은 심사용, 이건 셀프 점검용"*이다.

---

## 참고문헌

**성숙도 모델 (조상)**
- Capability Maturity Model Integration — https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration
- SCAMPI (Standard CMMI Appraisal Method) — https://en.wikipedia.org/wiki/Standard_CMMI_Appraisal_Method_for_Process_Improvement

**AI 성숙도 모델**
- CMU SEI, *The AI Adoption Maturity Model v1.0* (2026-06-30) — https://www.sei.cmu.edu/library/ai-adoption-maturity-model/
- SEI 보도 — https://www.sei.cmu.edu/news/sei-and-accenture-release-ai-adoption-maturity-model-to-help-organizations-scale-ai-with-predictable-outcomes/
- Accenture 뉴스룸 (2026) — https://newsroom.accenture.com/news/2026/accenture-and-the-carnegie-mellon-university-software-engineering-institute-launch-ai-adoption-maturity-model-to-help-organizations-scale-ai-with-predictable-outcomes
- MIT CISR, *Building Enterprise AI Maturity* (2024-12-19) — https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian
- MIT CISR, *Grow Enterprise AI Maturity for Bottom-Line Impact* (2025-08-21) — https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer
- MIT Sloan, *What's your company's AI maturity level?* — https://mitsloan.mit.edu/ideas-made-to-matter/whats-your-companys-ai-maturity-level
- VKTR 해설 — https://www.vktr.com/ai-technology/mits-4-stages-of-enterprise-ai-maturity/
- Gartner 보도자료 (2025-06-30) — https://www.gartner.com/en/newsroom/press-releases/2025-06-30-gartner-survey-finds-forty-five-percent-of-organizations-with-high-artificial-intelligence-maturity-keep-artificial-intelligence-projects-operational-for-at-least-three-years
- Gartner AI Maturity Model 공식 초록 (2024-11-20) — https://www.gartner.com/en/documents/5937907
- Gartner AI Maturity Model Toolkit — https://www.gartner.com/en/chief-information-officer/research/ai-maturity-model-toolkit
- Cisco AI Readiness Index 2025 (PDF) — https://www.cisco.com/c/dam/m/en_us/solutions/ai/readiness-index/2025-m10/documents/cisco-ai-readiness-index-2025-realizing-the-value-of-ai.pdf
- Cisco 뉴스룸 (2025-10) — https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2025/m10/cisco-ai-research-the-most-ai-ready-companies-outpace-peers-in-the-race-to-value.html
- Cisco Look-up Tool (셀프 진단) — https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index/lookup-tool.html

**학술**
- Sadiq et al., *Artificial intelligence maturity model: a systematic literature review* (2021) — https://pmc.ncbi.nlm.nih.gov/articles/PMC8409328/
- Pöppelbuß & Röglinger, *What makes a useful maturity model?* (ECIS 2011) — https://aisel.aisnet.org/ecis2011/28/
- *Exploring the Limitations of Business Process Maturity Models: A Systematic Literature Review* (2024) — https://www.tandfonline.com/doi/full/10.1080/10580530.2024.2332210
- Mettler, *Maturity assessment models: a design science research approach* (2011) — https://scispace.com/papers/maturity-assessment-models-a-design-science-research-3bc05eg42j
- *A sociotechnical perspective for responsible AI maturity models* — https://www.sciencedirect.com/science/article/pii/S266709682300040X
- *Human-Centered AI Maturity Model (HCAI-MM)* — https://arxiv.org/pdf/2512.14977
- *AI Maturity in SMEs: Internalized and Ecosystem-Embedded Capabilities* — https://arxiv.org/pdf/2603.08728
