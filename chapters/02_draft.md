---
장: 2장. 이미 나와 있는 자들, 그리고 그들이 비워둔 자리
버전: draft-2
작성: 2026-08-14
반영: review_02_03.md #2·#6·#9·#12·#13 / DEDUP_DECISIONS.md 재정 A·E (검증 배치와 없는 것 둘을 발견에서 멈추고 설계 결론은 뒤 장으로 넘김)
---

# 2장. 이미 나와 있는 자들, 그리고 그들이 비워둔 자리

<figure class="editorial-figure">
<img src="assets/images/ch02-existing-rulers-gaps.webp"
     srcset="assets/images/ch02-existing-rulers-gaps-704.webp 704w, assets/images/ch02-existing-rulers-gaps.webp 1408w"
     sizes="(max-width: 736px) calc(100vw - 2.5rem), 704px"
     alt="정교한 대형 측정 장치의 눈금이 자원 연결과 사람 간 인계 구간에서 비고, 손이 작은 자에 새 눈금을 그리는 삽화"
     width="1408" height="939" loading="lazy" decoding="async" />
<figcaption>좋은 자도 다른 조직을 위해 만들어졌다면 우리가 아픈 자리에 빈 눈금을 남긴다.</figcaption>
</figure>

자를 만들어보기로 하고 자료를 뒤지던 며칠째, 124쪽짜리 AI 성숙도 모델을 만났다. 다섯 단계, 여덟 개 차원, 스물일곱 개 역량영역. 발표는 2026년 6월이고, 낸 곳은 카네기멜런대학교 소프트웨어공학연구소다. 줄여서 SEI라고 부르는 그곳, **CMMI를 만든 바로 그 조직**이다.[^c2n1]

그 대목에서 손이 멈춘다. 나에게 이건 남의 소식이 아니다. 10년 동안 내가 들고 다니던 자를 만든 사람들이, AI 시대에 맞춰 새 자를 깎아서 내놓은 것이다. 그렇다면 하나 더 만들 이유가 남아 있기는 할까?

답을 내려면 일단 그 자를 제대로 들여다봐야 했다. 같이 들여다보자.

## 규모로 겨루자면 승부는 시작 전에 끝나 있다

먼저 이 모델이 어떻게 만들어졌는지부터 보자. 기존에 나와 있던 AI 성숙도 시도를 100건 넘게 훑었고, 그중 서른여섯 개 이상은 정밀하게 뜯어봤다. 임원 스무 명에서 스물다섯 명을 인터뷰하고, 실무자 약 600명에게 설문을 돌렸다. 그리고 포춘 500대 기업 여러 곳에서 실제로 파일럿을 굴려 검증했다.[^c2n2]

이 목록을 처음 읽었을 때의 기분을 솔직히 적어두는 편이 낫겠다. 김이 좀 빠졌다. 혼자 노트에 축을 그려가며 몇 주를 보낸 사람 앞에 저런 이력서가 놓이면, 이게 겨뤄볼 만한 판인가 싶어진다. 규모로 붙자면 이 승부는 시작 전에 끝나 있다.

그러니 그 이야기부터 하고 넘어가자. **잘 만든 모델이다.** 40년 동안 성숙도 모델을 만들어온 조직이 그 자산을 그대로 얹어 만들었고, 읽어보면 그게 문장마다 드러난다. 역량영역마다 "이런 산출물이 있으면 그 역량이 있다고 볼 만하다"는 예시를 붙여둔 것도 그렇고, 바로 그 옆에 산출물과 증거가 일대일로 대응하지는 않는다고 못 박아 둔 것도 그렇다.[^c2n1] 체크리스트를 채우는 놀이로 변질됐던 과거를 만든 장본인들이, 자기 문서 안에 그 경고를 먼저 써넣은 것이다. 이건 아무나 쓸 수 있는 문장이 아니다.

인정하지 않고 시작하면 뒤에 할 이야기가 전부 헐거워진다. 그러니 "그들이 부족하다"는 말로는 한 줄도 나아가지 말자.

## 게다가 하려던 말까지 거의 같았다

더 곤란한 건 그다음이었다. 규모만 앞선 게 아니라, 하려던 말까지 비슷했다. 원문에 이런 문장이 있다.

> 진짜 AI 성숙도는 조직이 얼마나 많은 AI를 배포했느냐가 아니라, 신뢰할 수 있고 회복력 있는 역량과 엄정한 엔지니어링 실천, 그리고 사업 성과에 정렬된 거버넌스를 만들어낼 능력으로 측정된다.[^c2n1]

이 문장을 읽고 한참 앉아 있었다. 얼마나 깔았느냐가 아니라 믿을 만하게 만들 능력이라니, 우리가 앞 장에서 도구 이야기를 하며 짚었던 바로 그 지점이다. 앞서 나간 사람이 같은 자리를 먼저 찍어놓은 걸 발견하면 기분이 묘해진다. 억울한 것 같기도 하고 반가운 것 같기도 하다.

그렇다면 이 문장을 어떻게 다뤄야 할까? 못 본 척 숨기는 방법도 있다. 하지만 그러지 말자. 오히려 앞에 내세우는 편이 낫다. **성숙도 모델의 원조를 만든 조직이 독립적으로 같은 결론에 도달했다면, 그건 우리 주장이 흔들린다는 뜻이 아니라 그 방향이 맞다는 두 번째 증거다.** 서로 다른 두 곳이 같은 곳을 가리키면 논증은 약해지는 게 아니라 단단해진다.

그러니 이 책이 만들려는 자는 "우리가 처음"이라고 말하는 물건이 아니다. **"우리는 다르게 본다"**고 말하는 물건이다. 그렇다면 정확히 어디가 다른가. 그걸 찾느라 문서를 한 번 더 읽었고, 두 번째 읽기에서 예상 못 한 걸 발견했다.

## 세어보다가 생각이 바뀌었다

두 번째로 읽을 때는 내용이 아니라 배치를 봤다. 이 모델은 역량영역 하나하나가 특정 단계에 걸려 있는 구조다. 그러니까 "이 역량영역의 목표를 다 채워야 그 차원이 몇 단계에 도달한다"는 식으로, 역량영역마다 소속 단계가 붙어 있다.

그래서 그냥 세어봤다. 단계가 명시된 스물다섯 개가 어디에 걸려 있는지.

1단계에 둘. **2단계에 열하나. 3단계에 열.** 4단계에 하나. 5단계에 하나.[^c2n1]

세어놓고 숫자를 한참 들여다봤다. 가운데 두 단계에만 스물하나, **전체의 84퍼센트가 몰려 있다.** 위의 두 단계에는 각각 하나씩만 있다. 다섯 단계짜리 모델인데 무게는 아래쪽 절반에 다 실려 있는 셈이다. 며칠 동안 문장을 따라 읽을 때는 보이지 않던 것이 반나절 손으로 세자 드러났다. 이때부터는 개별 항목보다 분포 자체를 읽어야 했다.

::: {.reading-aid .stat-dashboard .stat-dashboard--compact}
### SEI 모델, 25개 역량영역으로 읽기

<p class="stat-caption">단계가 명시된 역량영역의 분포</p>
<div class="stat-chart stat-stage-distribution" role="img" aria-label="단계가 명시된 SEI 역량영역 25개 가운데 1단계 2개, 2단계 11개, 3단계 10개, 4단계 1개, 5단계 1개다. 2단계와 3단계를 합하면 21개로 전체의 84퍼센트다.">
<div class="stat-row"><span class="stat-series">1단계</span><svg class="stat-mini-bar" viewBox="0 0 100 10" preserveAspectRatio="none" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"><rect class="stat-bar-track" x="0" y="0" width="100" height="10" /><rect class="stat-fill stat-fill--compare" data-value="8" x="0" y="0" width="8" height="10" /></svg><strong class="stat-value">2개</strong></div>
<div class="stat-row"><span class="stat-series">2단계</span><svg class="stat-mini-bar" viewBox="0 0 100 10" preserveAspectRatio="none" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"><rect class="stat-bar-track" x="0" y="0" width="100" height="10" /><rect class="stat-fill stat-fill--leader" data-value="44" x="0" y="0" width="44" height="10" /></svg><strong class="stat-value">11개</strong></div>
<div class="stat-row"><span class="stat-series">3단계</span><svg class="stat-mini-bar" viewBox="0 0 100 10" preserveAspectRatio="none" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"><rect class="stat-bar-track" x="0" y="0" width="100" height="10" /><rect class="stat-fill stat-fill--leader" data-value="40" x="0" y="0" width="40" height="10" /></svg><strong class="stat-value">10개</strong></div>
<div class="stat-row"><span class="stat-series">4단계</span><svg class="stat-mini-bar" viewBox="0 0 100 10" preserveAspectRatio="none" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"><rect class="stat-bar-track" x="0" y="0" width="100" height="10" /><rect class="stat-fill stat-fill--compare" data-value="4" x="0" y="0" width="4" height="10" /></svg><strong class="stat-value">1개</strong></div>
<div class="stat-row"><span class="stat-series">5단계</span><svg class="stat-mini-bar" viewBox="0 0 100 10" preserveAspectRatio="none" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"><rect class="stat-bar-track" x="0" y="0" width="100" height="10" /><rect class="stat-fill stat-fill--compare" data-value="4" x="0" y="0" width="4" height="10" /></svg><strong class="stat-value">1개</strong></div>
</div>

<p class="stat-note">막대 길이는 전체 25개 가운데 각 단계가 차지하는 비중이다. 숫자는 역량영역의 개수로 표시했다.</p>
<p class="stat-takeaway"><strong>2~3단계에 21개, 전체의 84퍼센트.</strong> SEI 모델은 초기·중간 단계의 역량을 특히 촘촘하게 다룬다.</p>
:::

## 분포가 곧 세계관이다

이 분포는 모델의 무게가 어디에 실려 있는지를 보여준다. **초기·중간 단계의 역량을 특히 촘촘하게 다룬다.** 왜 그렇게 배치했는지까지 숫자만으로 단정할 수는 없다.

이렇게 읽으면 앞뒤가 맞는다. 데이터를 정비하고, 엔지니어링 역량을 세우고, 거버넌스를 걸고, 테스트를 붙이는 일. 이게 전부 2단계에 몰려 있다. 그다음 워크플로를 다시 짜고 측정 체계를 붙이는 일이 3단계다. 여기까지 오면 확장과 미래대비는 각각 역량영역 하나면 족하다고 본 것이다. 상위 단계보다 초기 구축에 더 많은 역량영역을 배치한 구조다.

이 세계관이 가장 선명하게 드러나는 자리가 검증이다. SEI 모델에도 검증을 다루는 역량영역이 분명히 있다. 이름은 `Test and Evaluation`이고, 내용도 만만치 않다. 데이터 드리프트나 환각처럼 AI 특유의 문제를 잡아내는 전문 테스트를 정의하라고 하고, 매번 같은 답이 나오지 않는 기능의 출력을 어떻게 기준선화할지 정하라고 하고, 생성형 AI의 결과까지 포함해 테스트를 자동화할 수 있게 하라고 한다.[^c2n1] 읽어보면 우리가 실제로 부딪히는 문제들이 거의 다 들어 있다.

그런데 이 역량영역이 걸려 있는 자리가 **2단계**다.

무슨 뜻일까? 검증은 배포하려면 당연히 갖춰야 하는 기초 위생이라는 뜻이다. 손 씻고 수술실에 들어가는 것과 같다. 갖췄다고 성숙한 게 아니라, 안 갖추면 아예 시작하면 안 되는 것.

여기서 한 걸음 물러서자. 이 배치가 틀렸다고 말하려는 게 아니다. 배치란 만든 사람들이 본 조직의 모습을 그대로 옮겨놓은 것이고, 그렇게 생긴 조직은 세상에 아주 많다.

1장에서 확인한 공백은 기초보다 **만든 다음**에 몰려 있었다. 이 차이만 옆에 놓자. SEI의 배치는 앞쪽이 아직 안 채워진 조직을 정확히 재지만, 이미 만들 줄 아는 조직이 그다음에서 멈췄을 때는 다른 눈금이 필요할 수 있다. 여기서는 결론을 서두르지 않고, 모델의 무게가 기초에 실려 있다는 사실까지만 확인해두자.

## 그들에게 아예 없는 것 둘

여기까지는 같은 것을 다르게 배치한 이야기다. 그런데 배치의 차이가 아니라 아예 없는 것도 있었다. 원문 전체를 검색해서 확인한 것이 둘이다.

첫째, **예산과 자원을 다루는 축이 없다.** 대응하는 역량영역이 아예 없고, 예산이라는 단어는 "자원에는 인력과 자금이 포함된다" 정도의 부속 언급으로 딱 한 번 나온다.[^c2n1]

둘째, **담당자가 바뀔 때 어떻게 넘기는지를 묻지 않는다.** 인계, 승계, 소유권 이전에 해당하는 표현이 124쪽 어디에도 없다.[^c2n1]

왜 이 둘이 빠졌는지는 원문이 설명하지 않는다. 포춘 500대 기업을 포함해 검증했다는 사실만으로 예산과 인계가 자동 해결된다고 단정할 수도 없다. 여기서는 이유를 추측하지 말고, 두 항목이 독립 역량으로 다뤄지지 않는다는 사실만 확인하자.

그런데 우리 자리에서는 어떤가. 이런 장면을 떠올려보자. 파일럿이 잘 끝나서 이제 실제로 운영에 올리려는데, 그때부터 쓸 자원을 어디서 어떻게 받아야 하는지가 정해져 있지 않다. 안내 문서는 있는데 그건 신청하는 법이고, 계속 쓸 몫을 배분하는 규칙은 아무 데도 없다. 그래서 매년 취합과 삭감만 반복된다. 혹은 이런 장면. 잘 돌던 것을 만든 사람이 부서를 옮긴다. 인수인계 문서는 형식대로 넘어갔는데, 왜 그렇게 만들었는지는 그 문서에 없다. 반년 뒤에 문제가 생기면 아무도 손을 못 댄다.

두 장면은 이 책이 재려는 문제에 정확히 들어온다. 그런데 124쪽짜리 SEI 모델에서도 독립된 눈금으로는 보이지 않는다. 자기 조직에서 제일 아픈 데를 재려고 자를 들었는데 거기에 눈금이 없는 걸 알았을 때, 그 기분은 좀 서늘하다. 일단 빈틈 둘을 찾았다. 지금 손에 쥔 건 거기까지다. 그 자리에 눈금을 새길지 말지, 새긴다면 어떤 이름을 붙일지는 축을 짜는 장에서 정하자.

## 마지막 빈틈은 규모다

이제 다른 자들도 짧게 짚고 가자. MIT의 연구는 721개 기업 설문을 직접 근거로 둔다. 1장에서 본 그 분포와 재무성과 상관이 거기서 나왔다. 공식 브리핑 본문과 단계 구간은 공개돼 있지만, 같은 방식으로 우리 조직의 입력값을 넣어 계산할 공개 설문지는 없다. 즉 구조는 읽을 수 있어도 그 자를 그대로 들고 우리 조직을 재기는 어렵다. Gartner의 모델은 다섯 수준에 일곱 개 기둥으로 잘 짜여 있고 툴킷도 딸려 있지만 전체 지침은 유료 구독자만 쓴다. Cisco는 무료 셀프 진단 도구도 열어두고 있다. 다만 성격이 다르다. 그건 남과 비교해서 내가 어디쯤인지 알려주는 벤치마크지, 그래서 다음에 뭘 하라는 처방이 아니다.[^c2n3]

그리고 SEI 모델로 돌아오면, 마지막 빈틈이 남아 있다. **규모다.**

124쪽에 여덟 개 차원, 스물일곱 개 역량영역, 그 아래 목표와 실천 항목이 수백 개다. 유료도 아니고 심사를 강제하지도 않으니 접근만 놓고 보면 열려 있다. 그런데 열려 있다는 것과 쓸 수 있다는 건 다른 이야기다. 팀장 한 명이 오후에 혼자 이걸 다 돌릴 수 있을까? 124쪽과 27개 역량영역을 15분 안에 대조하기는 어렵다. 그러면 자연스럽게 사람을 붙이게 되고, 사람을 붙이면 일정이 생기고, 일정이 생기면 준비 자료를 만들게 된다. 그리고 준비 자료를 만들기 시작하는 순간, 도입부에서 말한 그 실패가 다시 시작된다.

**그래서 30문항, 15분이다.** 이건 대충 하자는 뜻이 아니라 설계다. 오늘 오후에 혼자, 결재 없이 끝낼 수 있는 크기가 아니면 애초에 두 번째 진단까지 이어지기 어렵기 때문이다. 한 번 재고 마는 자는 자가 아니다.

SEI 모델의 단계 정의와 여덟 차원, 역량영역의 구성이 궁금하다면 부록 C에 따로 정리해 두었다. 여기서는 논지만 붙들고 가자.

::: {.leader-summary}

## 다음 보고에서 쓸 것

**하나.** SEI 모델은 기존 시도 100건 이상, 실무자 약 600명 설문과 포춘 500대 기업 파일럿을 거친 좋은 자다. AXMM은 그것을 무시하고 새로 시작한 모델이 아니다.

**둘.** 다만 무게중심이 다르다. 단계가 명시된 역량영역의 84퍼센트가 가운데 두 단계에 몰려 있고 검증도 2단계에 있다. 자원·비용과 담당자 인계는 독립 항목으로 다루지 않는다.

**셋.** 모델을 고를 때는 지난 분기에 가장 오래 붙든 문제 세 개가 그 목차 어디에 들어가는지 대보자. **우리 조직에서 제일 아픈 데를 재지 못하면 좋은 자여도 우리 자는 아니다.**

:::

## 마무리

이 장에서 확인한 걸 한 줄로 줄이면 이렇다. 이미 나와 있는 자들은 잘 만들어졌고, 다만 다른 곳을 보라고 만들어졌다. 우리가 할 일은 그걸 깎아내리는 게 아니라, 그들이 보지 않은 자리에 눈금을 새기는 것이다.

그런데 여기서 마음이 편해지면 곤란하다. 지금까지 우리는 성숙도 모델들끼리 비교했을 뿐이다. **성숙도 모델이라는 물건 자체가 쓸모없다는 비판**은 아직 하나도 다루지 않았다. 그리고 그 비판은 꽤 오래됐고, 꽤 날카롭고, 상당 부분 맞다. 단계로 줄 세우는 게 무슨 근거가 있느냐, 등급이 붙는 순간 조작이 시작되지 않느냐, 재고 나서 뭘 하라는 말은 왜 없느냐.

이런 말을 들으면 방어하고 싶어진다. 하지만 자를 내놓는 사람이 그 약점을 먼저 말하지 않으면 결국 다른 사람이 말한다. 그래서 이어지는 장은 성숙도 모델을 변호하지 않고, 오래된 비판 가운데 무엇이 맞는지부터 인정하며 시작한다.

---

[^c2n1]: Carnegie Mellon University SEI, *The AI Adoption Maturity Model v1.0* (2026-06-30), 124쪽. 본문의 인용문, 역량영역의 단계 귀속과 그 분포, `Test and Evaluation` 역량영역의 목표·실천 내용, 예시 산출물에 관한 경고, 예산 언급 빈도와 인계 관련 표현의 부재는 모두 공개된 원문 PDF를 직접 확인한 것이다. — https://www.sei.cmu.edu/library/ai-adoption-maturity-model/ / PDF: https://www.sei.cmu.edu/documents/6534/The_AI_Adoption_Maturity_Model.pdf

[^c2n2]: 모델 개발 규모(기존 시도 100건 이상 검토, 임원 인터뷰 20~25명, 실무자 약 600명 설문, 포춘 500대 기업 파일럿)는 SEI·Accenture의 발표 자료와 원문 서문에 근거한다. 설문은 SEI와 Accenture의 자체 조사(2026-01)임을 밝혀둔다. — SEI 보도자료, https://www.sei.cmu.edu/news/sei-and-accenture-release-ai-adoption-maturity-model-to-help-organizations-scale-ai-with-predictable-outcomes/ / Accenture 뉴스룸, https://newsroom.accenture.com/news/2026/accenture-and-the-carnegie-mellon-university-software-engineering-institute-launch-ai-adoption-maturity-model-to-help-organizations-scale-ai-with-predictable-outcomes

[^c2n3]: MIT CISR 공식 브리핑은 2022년 721개 기업 조사와 단계 판정 방식, 2025년 152개 기업 후속 조사까지 본문을 공개한다. 다만 누구나 같은 점수를 계산할 독립 셀프 진단은 제공하지 않는다 — https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian / https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer. Gartner의 공개 초록은 5수준·7기둥을 설명하지만 전체 툴킷은 고객 전용이다 — https://www.gartner.com/en/documents/5937907. Cisco는 AI Readiness Index와 함께 무료 셀프 진단을 운영한다 — https://www.cisco.com/c/m/en_us/solutions/ai/readiness-index/lookup-tool.html
