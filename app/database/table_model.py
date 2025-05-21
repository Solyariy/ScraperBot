from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()

class DisciplineTable(Base):
    __tablename__ = "disciplines"

    id_: Mapped[int] = mapped_column(name="id", primary_key=True)
    code: Mapped[int]
    name: Mapped[str]
    specialty: Mapped[str]
    kind: Mapped[str]
    semester: Mapped[str | None]
    year: Mapped[int]
    credits_ects: Mapped[str | None]
    hours: Mapped[str | None]
    students_max: Mapped[str | None]
    groups_max: Mapped[str | None]
    one_group_range: Mapped[str | None]
    faculty: Mapped[str]
    cathedra: Mapped[str]
    education_level: Mapped[str]
    lecturer: Mapped[str | None]

