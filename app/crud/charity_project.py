from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base_crud import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    @staticmethod
    async def get_project_by_name(
        name: str,
        session: AsyncSession
    ) -> Optional[CharityProject]:
        charity_project = await session.execute(
            select(CharityProject).where(
                CharityProject.name == name
            )
        )
        return charity_project.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)