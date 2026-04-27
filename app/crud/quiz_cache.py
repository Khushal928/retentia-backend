import json
import logging
from redis.exceptions import RedisError
from app.utils.redis_client import redis_client

logger = logging.getLogger(__name__)
QUIZ_TTL = 3600  # 60 mins

def store_quiz(quiz_id: str, user_id: int, questions: list):
    try:
        redis_client.setex(
            f"quiz:{quiz_id}",
            QUIZ_TTL,
            json.dumps({
                "user_id": user_id,
                "questions": questions
            })
        )
        return True
    
    except RedisError:
        logger.exception("Failed to cache quiz %s in Redis", quiz_id)
        return False

def get_quiz(quiz_id: str, user_id: int):
    try:
        data = redis_client.get(f"quiz:{quiz_id}")

        if not data:
            logger.exception("quiz %s expired", quiz_id)
            return None

        if (data.user_id != user_id):
            logger.exception("user %i tried to submit quiz %s which is not created by them", user_id, quiz_id)
            return None

    quiz_data = json.loads(data)
    return [QuizQuestion(**q) for q in quiz_data["questions"]]

    except RedisError:
        logger.exception("Failed to fetch quiz %s from Redis", quiz_id)
        return None