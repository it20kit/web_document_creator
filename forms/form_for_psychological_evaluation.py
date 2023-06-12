from pydantic import BaseModel


class FormForPsychologicalEvaluation(BaseModel):
    """Описывает все поля формы для создания документа психологической оценки ребенка"""
    date_of_verification: str
    fio: str
    date_of_birth: str
    visited_group: str
    reason_for_examination: str
    nature_of_diagnosis: str
    methods: str

    means_of_communication: str | None = None
    features_of_child_contact: str | None = None
    emotional_reaction: str | None = None
    reaction_to_approval: str | None = None
    reaction_to_remark: str | None = None
    reaction_to_failure: str | None = None
    emotional_state: str | None = None
    communication: str | None = None
    reaction_to_the_result: str | None = None

    presence_and_persistence: str | None = None
    understanding_instructions: str | None = None
    indicative_activity: str | None = None
    independence_of_completing_tasks: str | None = None
    nature_of_activity: str | None = None
    pace_and_dynamics_of_activity: str | None = None
    efficiency: str | None = None
    features_of_regulation_of_activity: str | None = None
    organization_of_assistance: str | None = None

    features_of_attention: str | None = None
    features_of_perception: str | None = None
    memory_features: str | None = None
    features_of_thinking: str | None = None
    features_of_speech: str | None = None
    features_of_imagination: str | None = None
    features_of_motor_function: str | None = None
    features_of_large_motor_skills: str | None = None

    conclusion: str | None = None
    forecast: str | None = None
    conclusions_about_dynamics: str | None = None
    general_recommendations: str | None = None
    recommendations_to_parents: str | None = None
