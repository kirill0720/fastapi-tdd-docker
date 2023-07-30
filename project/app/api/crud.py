from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary, SummarySchema


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> SummarySchema | None:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None
