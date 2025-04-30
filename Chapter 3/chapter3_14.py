from pydantic import BaseModel, field_validator

class Article(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    @field_validator("title")
    @classmethod
    def check_title(cls, v: str)->str:
        if "FARM stack" not in v:
            raise ValueError("Title must contain 'FARM stack'")
        
        return v.title()
    
article_data = {
    "id": 1,
    "title": "FARM stack",
    "content": "This is a content",
    "published": True
}
article = Article.model_validate(article_data)
print(article)