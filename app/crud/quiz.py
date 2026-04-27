from typing import List
from app.schemas.quiz import QuizQuestion, UserResponse
from supermemo2 import first_review, review

def evaluate_quiz(user_id: int, quiz_data: List[QuizQuestion], user_responses: List[UserResponse]):
    for i in user_responses:
        






class UserResponse(BaseModel):
    question_id: int
    submitted_answer: str

class QuizQuestion(BaseModel):
    question_id: int
    chapter: str
    question: str
    options: List[str] = Field(min_length=4, max_length=4)
    correct_answer: str
    related_concepts: List[str]