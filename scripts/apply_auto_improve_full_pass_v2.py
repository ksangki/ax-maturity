#!/usr/bin/env python3
"""Exact-match corrections for the reviewed full-book pass.

The base pass intentionally aborts if any FIND no longer matches the current branch.
This wrapper corrects the six drifted FIND blocks discovered by the first dry run,
then delegates to the same all-or-nothing validator/applier.
"""

from __future__ import annotations

from apply_auto_improve_full_pass import EDITS, main


def replace_by_label(path: str, label: str, old: str, new: str | None = None) -> None:
    edits = EDITS[path]
    for index, (_old, current_new, current_label) in enumerate(edits):
        if current_label == label:
            edits[index] = (old, current_new if new is None else new, current_label)
            return
    raise RuntimeError(f"edit label not found: {path}: {label}")


# Chapter 2: current reviewed prose differs slightly from the first captured snippets.
replace_by_label(
    "chapters/02_draft.md",
    "SEI 분포에서 설계자의 의도를 추론하던 문장 제거",
    "우연이 아니다. 이 배치는 만든 사람들의 판단을 그대로 드러낸다. **어려운 건 기초를 갖추는 일이라는 판단이다.**",
    "이 분포는 모델의 무게가 어디에 실려 있는지를 보여준다. **초기·중간 단계의 역량을 특히 촘촘하게 다룬다.** 왜 그렇게 배치했는지까지 숫자만으로 단정할 수는 없다.",
)
# The following sentence makes the same unsupported author-intent inference, so keep
# the section internally consistent rather than fixing only its first sentence.
EDITS["chapters/02_draft.md"].append(
    (
        "기초를 제대로 쌓으면 그 위는 자연히 따라온다는 세계관이다.",
        "상위 단계보다 초기 구축에 더 많은 역량영역을 배치한 구조다.",
        "SEI 분포 해석의 반복 추론 제거",
    )
)
replace_by_label(
    "chapters/02_draft.md",
    "세계 최고 수준이라는 불필요한 비교 단정 축소",
    "두 장면 다 성숙도의 문제이고, 팀장이 가장 먼저 부딪히는 벽이다. 그런데 세계에서 가장 정교한 자에는 그걸 잴 눈금이 없다.",
)
replace_by_label(
    "chapters/02_draft.md",
    "유일성 주장 제거",
    "Cisco는 무료 셀프 진단 도구를 열어둔 거의 유일한 곳인데, 성격이 다르다. 그건 남과 비교해서 내가 어디쯤인지 알려주는 벤치마크지, 그래서 다음에 뭘 하라는 처방이 아니다.[^c2n3]",
    "Cisco는 무료 셀프 진단 도구도 열어두고 있다. 다만 성격이 다르다. 그건 남과 비교해서 내가 어디쯤인지 알려주는 벤치마크지, 그래서 다음에 뭘 하라는 처방이 아니다.[^c2n3]",
)

# Chapter 3: punctuation/spacing around the three captured passages differed.
replace_by_label(
    "chapters/03_draft.md",
    "검증 필요성을 절대 명제로 쓰던 표현 완화",
    "여러 사람이 여러 개를 굴리기 시작하면 그때부터 검증 없이는 한 걸음도 못 나간다.",
)
replace_by_label(
    "chapters/03_draft.md",
    "문헌고찰 범위 밖으로 확장된 전칭 주장 축소",
    "같은 문헌고찰에 문장이 하나 더 있다. 기존 AI 성숙도 모델을 실제 조직에 **적용해본 연구가 한 건도 없었다**는 것이다.[^c3n1] 0건이다.",
    "같은 문헌고찰에 문장이 하나 더 있다. **이 연구가 검토한 문헌들에서는** 기존 AI 성숙도 모델을 실제 조직에 적용한 연구가 한 건도 확인되지 않았다.[^c3n1] 0건이다.",
)
replace_by_label(
    "chapters/03_draft.md",
    "임의의 횟수와 필연적 행동을 제거",
    "**셋,** 결과를 받아 놓고 아무것도 하지 않는 일이 두 번 반복되는 순간이다. 세 번째 진단에는 아무도 성실하게 답하지 않는다. 사람들은 답을 대충 적는 게 아니라, 이 조직에서 재는 일이 아무 결과도 낳지 않는다는 걸 정확히 학습한 것이다.",
    "**셋,** 결과를 받아 놓고 아무것도 하지 않는 일이 반복되는 순간이다. 다음 진단에서는 응답의 성실성을 기대하기 어려워진다. 재는 일이 아무 결과도 낳지 않는다는 경험이 쌓이기 때문이다.",
)


if __name__ == "__main__":
    raise SystemExit(main())
