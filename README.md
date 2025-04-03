# 설치할 라이브러리

```bash
pip install fastapi uvicorn beanie
```


# Git

```bash
git init
New-Item .gitignore

git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://깃헙레포주소.git
git push -u origin main
```

# 구조
```bash
root
|--src/
|   |--models/
|   |--routes/
|   |--main.py
|--.gitignore
|--pyproject.toml
|--README.md
```

# 실행
```shell
uvicorn src.main:app --reload
```

# 플래너 만들기

* `로그인` 기능
    * `이메일`, `비밀번호`
* `이벤트` 추가, 삭제, 업데이트
    * `제목`, `이미지`, `설명`, `태그`, `위치`, `날짜`