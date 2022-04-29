# 기여 가이드

---

## 기여하기 전

---

TheAlgorithms/Python에 오신 것을 환영합니다! Pull Request를 보내기 전에 이 가이드라인을 충분히 읽어주세요.
기여 가이드에 대한 의문점은 [이슈](https://github.com/TheAlgorithms/Python/issues/new, "이슈")나 [Gitter Community](https://gitter.im/TheAlgorithms, "Gitter")를 통해 부담없이 알려주세요.

## 기여하기

---

### 기여자

- 표절 금지
- merge 이후에는 MIT License를 갖게 됨.
- 스타일과 표준을 만족시켜야 함.
- 문제의 새로운 풀이나 자료구조 혹은 알고리즘의 또다른 구현 방법에 대해서 구현할 수 있지만 기존에 있는 코드와 동일한 방식의 구현은 받아들여지지 않음.
- Pull Request 전에 이미 구현되었는지를 먼저 확인해야 함.

### 기여

- 복잡한 알고리즘에 대한 주석의 문법적인 실수를 고쳐주면 좋음.
- 기여자의 코드는 GitHub Action을 통해 자동으로 테스트됨.
- PR 이후, GitHub Action이 해당 PR 페이지의 아래부분에 실행되는 것을 확인해야 함.
- 테스트가 실패할 경우, <i>details</i>버튼을 통해 자세한 정보를 확인할 수 있음.
- 이해가 안된다면, 해당 PR 페이지에 코멘트를 남기면 도와줄 수 있음.
- 이슈 페이지를 정리할 수 있게 커밋 메시지를 `fixes: #{$ISSUE_NO}`로 입력하여 머지됐을 때 자동으로 이슈가 닫힐 수 있도록 해야 함.

### 알고리즘 기여

알고리즘은 아래 조건을 충족하는 함수 혹은 클래스

- 한개 이상의 입력을 받아야 함.
- 내부적인 계산과 데이터의 변동을 구현.
- 한개 이상의 출력을 리턴해야 함.
- 부수적인 효과들은 최소한으로(ex: print(), plot(), read(), write()) 해야 함.
- 알고리즘은 독자들이 큰 프로그램에 사용하기 쉽게 패키지화 되어야 함
- 목적이 한눈에 들어오게 직관적인 클래스와 함수명 혹은 클래스명으로 해야 함.
- [Python naming conventions](https://peps.python.org/pep-0008/#naming-conventions)를 참고하여 직관적인 변수 이름을 사용해야 함.
- 다양한 입력 변수를 받을 수 있게 flexible하게 해야 함.
- **입력, 출력에 대한 파이썬 타입 힌트를 작성해야함**, [링크](https://docs.python.org/3/library/typing.html)
- **에러발생이 가능한 상황에서는 파이썬 Exception을 발생시켜야 함 (ValueError)**
- **파이썬 docs string을 이용하여 정확하게 설명하거나 소스에 대한 URL을 포함시켜야 함.**
- **유효한 케이스 및 에러가 발생할 수 있는 케이스에 대한 doctest를 포함시켜야 함.**

```py
def sum_ab(a, b):
"""
Return the sum of two integers a and b
>>> sum_ab(2, 2)
4
>>> sum_ab(-2, 3)
1
>>> sum_ab(4.9, 5.1)
10.0
"""
return a + b
```

- **계산 결과를 print나 plot이 아닌 리턴 형태로 해야함.**

### 코딩 스타일

- 설치

```bash
python3 -m pip install pre-commit
pre-commit install
```

- 실행: 아래 명령어를 통해서 모든 파일에 대해 스타일링을 실시하고 고칠 부분이 있으면 자동으로 고치고 커밋함.

```bash
pre-commit run --all-files --show-diff-on-failure
```

- 파이썬 3.9+ 이상의 문법으로 사용 print("Hello") o vs print "Hello" x
- `flake8 . --ignore=E203,W503 --maax-line-length=88`를 통과해야함

```bash
python3 -m pip install flake8
flake8 . --ignore=E203,W503 --max-line-length=88 --show-source
```

- **python doctest를 통해 docs string의 테스트케이스 테스트 수행**, [링크](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python)

```bash
python3 -m doctest -v my_submission.py
```

- **python의 input()함수 사용 불가**
- 배열 요소를 작업할 때는 lambda, map, filter, reduce등을 사용하는게 좋음.
- 파일 이름은 무조건 snake_style로 작성.

### 정리

1. 계산 로직은 함수형 프로그래밍으로 작성한다.
2. 함수 혹은 클래스메서드 입력 출력에 대한 파이썬 Type Hint를 작성하고 테스트를 진행한다.
   [테스트에 대한 문서](http://www.mypy-lang.org), [타입힌트에 대한 문서](https://docs.python.org/3/library/typing.html)
3. 함수 혹은 클래스메서등에 대해 python docs string을 통해 정확한 설명과 테스트케이스(유효, 에러)를 작성하고 doctest로 테스트를 진행한다.
   [테스트케이스 작성에 대한 문서](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python)
4. 에러케이스가 일어나는 입력에 대해서 `ValueError`등의 Exception을 발생시킨다.
