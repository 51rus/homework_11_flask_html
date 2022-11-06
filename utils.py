import json


def load_candidates_from_json() -> list[dict]:
    """Возвращает список всех кандидатов"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id: int) -> dict:
    """Возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """Возвращает кандидатов по имени"""
    result = []
    for name in load_candidates_from_json():
        if name['name'] == candidate_name:
            result.append(name)
    return result


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """Возвращает кандидатов по навыку"""
    result = []
    for skills in load_candidates_from_json():
        if skill_name in skills['skills'].lower().split(', '):
            result.append(skills)
    return result
