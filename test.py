import re
import json

request = {
    "date_of_verification": "11.06.23",
    "fio": "Дмитрий Анатольевич",
    "date_of_birth": "23.05.2017",
    "visited_group": "Солнышко",
    "reason_for_examination": "Агрессия",
    "nature_of_diagnosis": "Первичная",
    "methods": "Руденко Л.Г., Павлова Н.Н. Экспресс-диагностика в детском саду",

    "means_of_communication": "вербальное",
    "features_of_child_contact": "В контакт вступает легко",
    "emotional_reaction": "Заинтересованность",
    "reaction_to_approval": "Поощрение и одобрение вызывают окрашенную положительными эмоциями реакцию.",
    "reaction_to_remark": "После замечания старается исправить ошибку.",
    "reaction_to_failure": "Ребёнок обращается за оценкой правильности действий к взрослому",
    "emotional_state": "моциональный фон адекватный",
    "communication": "Активное",
    "reaction_to_the_result": "Свойственно понимание своих успехов и неудач",

    "presence_and_persistence": "Выраженный интерес в начале задания",
    "understanding_instructions": "Инструкция теряется, самоконтроль присутствует только в отношении части инструкции.",
    "indicative_activity": "Выраженная активность и целенаправленность при изучении объектов.",
    "independence_of_completing_tasks": "Не может самостоятельно начать и/или выполнять задание",
    "nature_of_activity": "Недостаточно активная",
    "pace_and_dynamics_of_activity": "Темп деятельности медленный",
    "efficiency": "Умеренная работоспособность",
    "features_of_regulation_of_activity": "Ошибки самостоятельно не замечаются",
    "organization_of_assistance": "Разъясняющая",

    "features_of_attention": "Внимание недостаточно устойчивое",
    "features_of_perception": "Различает и соотносит все фигуры",
    "memory_features": "Уровень развития зрительной кратковременной памяти - низкий.",
    "features_of_thinking": "Преобладающий вид мышления – наглядно-образное.",
    "features_of_speech": "Речь смазанная, невнятная.",
    "features_of_imagination": "Вербальное воображение имеет низкий уровень.",
    "features_of_motor_function": "Манипулятивная функция несколько ограничена",
    "features_of_large_motor_skills": "Имеются незначительные нарушения координации движений",

    "conclusion": "Актуальное развитие ниже показателей возрастной нормы",
    "forecast": "прогноз",
    "conclusions_about_dynamics": "вывод",
    "general_recommendations": "Подготовка и выдача рекомендаций педагогам",
    "recommendations_to_parents": "Консультация невролога. Консультация психиатра."
}

def compile_tempate(path, data):
    with open(path, 'r') as file:
        json_str = file.read()
        for k, v in data.items():
            pattern = "{{" + k + "}}"
            json_str = re.sub(pattern, v, json_str)
        data = json.loads(json_str)

        return data


print(compile_tempate('./templates/psychological_evaluation_form.json', request))

"""
Описание задачи:

Создать обработчики для блоков документа и фабрику, которая по типу блока создает обработчики.
Генерировать документ на основании шаблона. Пример смотри в файле test.py

"""