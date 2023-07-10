from pydantic import BaseModel

class encodings(BaseModel):
    support_calls: float
    total_spend: float
    usage_frequency: float
    tenure: float
    payment_delay: float
