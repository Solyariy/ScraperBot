from datetime import datetime

from ..database import DisciplineDao, get_postgres_manager


def delete_expired():
    now = datetime.now()
    with get_postgres_manager() as session:
        dao = DisciplineDao(session=session)
        deleted_disc = [
            discipline
            for discipline in dao.get_deleted()
            if (now - discipline.deletion_time).days > 30
        ]
        res = dao.hard_delete(deleted_disc)
    return res

if __name__ == '__main__':
    delete_expired()
