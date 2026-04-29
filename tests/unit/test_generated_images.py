from __future__ import annotations

from datetime import date

from app.utils.generated_images import create_section_fallback_svg


def test_create_section_fallback_svg_writes_public_asset(tmp_path):
    url = create_section_fallback_svg(
        run_date=date(2026, 4, 28),
        cluster_id="cluster-1",
        title="이미지 없는 AI 뉴스",
        summary="원본 이미지가 없을 때도 텍스트 전용 카드가 되지 않게 한다.",
        public_root=tmp_path,
    )

    assert url == "../assets/generated/2026-04-28/cluster-1.svg"
    svg_path = tmp_path / "assets" / "generated" / "2026-04-28" / "cluster-1.svg"
    assert svg_path.exists()
    assert "AI TREND" in svg_path.read_text(encoding="utf-8")
