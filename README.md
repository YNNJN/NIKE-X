# Pjt_NIKE x





<br>

<br>





## Crawler



<br>

### 1. 모든 페이지의 썸네일에 대한 크롤링

- 4월 7일

- NIKE > Collaboration 페이지의 썸네일 내용
  - 즉 제목(title), 작성 일자(date), 간단한 내용(content)에 대한 크롤러를 구현함
- `Requests`, `BeautifulSoup`의 라이브러리를 활용하여, csv 파일로 데이터를 추출함
  - 개발자 도구의 `copy selector`를 이용
- 카테고리 내 페이지 모두를 크롤링하기 위해 `url의 패턴`을 찾음
  - 도메인 주소 뒤 /page/#p 의 형태였기 때문에, 반복문을 활용함
- 페이지 수에 대한 반복문 내에 썸네일 수에 대한 반복문을 이중으로 작성하여
  - 모든 데이터를 딕셔너리 형태로 받음
- `with open`의 writer 권한으로 title, date, content를 필드 네임으로 하여 `DictWriter`로 csv 파일을 작성함
- 썸네일을 통한 본문 링크의 규칙 파악
  - 도메인 주소 뒤 제목을 소문자로 변환(lower()), 스페이스를 비롯한 기타 기호를 하이픈으로 변환(translate())의 규칙
  - 위의 규칙을 토대로 본문 내용 크롤링을 계획함



<br>

### 2. 모든 썸네일의 본문 링크에 대한 크롤링

- 4월 8일
- 전날 파악했던 본문 링크의 규칙이 하루만에 완전히 바뀌어버렸음을 확인함
  - 썸네일의 제목도, 요약도, 본문 중의 내용도 아닌 완전히 새로운 형태의 규칙이었음
  - 단 하루만에... 이것이 에자일인가요
  - 따라서 썸네일의 a 태그의 href를 크롤링하는 것으로 계획을 변경함

<br>

- copy하고 싶은 selector는 바로 이것이었는데,

  ```html
  body > div.content > div > div > div > div:nth-child(2) > article > div.col-md-6.feature-tile__content > a:nth-child(2)
  ```

  - 해당 태그가 class 등의 수식이 없는 순수한 a href 태그였기에, 기존의 방법으로는 해당 태그를 특정할 수 없었음

  - `re`를 import 하는

    ```python
    def not_lacie(href):
        return href and not re.compile("lacie").search(href)
    ```

    - 위의 방법을 찾아 모든 href를 가져왔고, csv 파일에서 순서를 확인하여 목표 태그가 위치하는 주기성을 파악하고자 했으나
    - 엑셀로 csv 파일을 여니 문서의 철자가 깨지면서 한글이 표기되는 이슈가 발생했음
      - 추후 확인한 바, 엑셀에서는 유니코드 정보를 포함하여 csv를 저장할 수 없기 때문에 발생하는 이슈라고 함
      - 메모장에서 실행한 후 인코딩을 utf-8로 선택하여 다른 이름으로 저장하고
      - 다른 이름으로 저장한 csv파일을 엑셀에서 다시 실행하여 해결할 수 있다고 함

<br>

- 공식문서를 통해 a 태그 하나만을 가져오는 방법을 찾음

  - [calling-a-tag](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all)

  - `find_all()`

    > If you need to get all the <a> tags, or anything more complicated than the first tag with a certain name, you’ll need to use one of the methods described in [Searching the tree](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree), such as find_all():

  - `find()`와 `find_all()`의 용례를 파악하고 적용함

    - tag와 class명의 표기 방식에 유의할 것

      ```python
      data = soup.find('div', {'class':"col-md-10"})
      contents = soup.find_all('div', {"class":"col-md-6 feature-tile__content"})
      ```

<br>

- soup 객체를 다루는 과정에서 라이브러리의 `__init__` 파일을 뜯어보기도 함
  - soup 객체를 스트링으로 변환했고
  - 큰따옴표의 인덱스로 슬라이싱하여 본문 링크를 추출할 수 있었음

- VSCode의 Go Definition 기능도 유용하게 사용함



<br>

### 3. 본문 내용에 대한 크롤링

- 4월 9일

- 본문 링크에 대한 csv 파일을 읽어옴

  - 본문 내용을 가져오기 위해 p 태그의 특정 class를 모두 가져옴
  - 추출한 데이터를 확인한 결과, 2016년 7월 12일자 게시물부터 적용한 클래스 규칙으로
  - 이전 게시물(30여 개)에 대해서는 다른 규칙을 적용하고 있음
    - 이전 게시물은 클래스 지정 없이 p태그 만으로 문단을 구성하고 있음
    - 따라서 해당 시점을 기준으로 데이터를 각각 추출하고 이후 병합해야


<br>

-  `.descendants` 

  > The `.descendants` attribute lets you iterate over all of a tag’s children, recursively: its direct children, the children of its direct children, and so on:

  - 이 개념을 활용하여 p 태그 하위의 태그들을 제외함

  ```python
  soup = BeautifulSoup(response, 'html.parser')
  
  contents = soup.find_all('p', class_='text--p')
  for content in contents:
      for child in content.descendants:
          if child is None:
              contents_list.append(child)
          else:
              contents_list.append(child)
  ```

  - 여전히 font-weight 관련과 이미지 캡션 관련 html 태그들이 데이터에 섞여있음
    - 하위 태그가 아니라서 섞여나오는 것 같음

- 본문의 끝을 명시하기 위해 '.....'의 문자열을 추가함



<br>

<br>



## 데이터 추출



<br>

### 1. NLTK, TextBlob 환경 설정

- 4월 10일

- MAC에서 환경 세팅 시 만난 에러

  - SSL Error

    - `punkt tokenizer`를  개별적으로 다운로드하여

    - OSX: `/usr/local/share/nltk_data/tokenizers` 의 경로에서 압축을 풂

      - 이 때 숨겨진 Library 폴더에 엑세스하기 위해 다음의 명령어 사용

        ```bash
        defaults write com.apple.finder AppleShowAllFiles YES
        ```

    - Python이 설치된 경로에 들어가 `Install Certificates.command`를 더블 클릭(First run)하여 해결

<br>

- 사용하는 인터프리터의 파이썬 버전을 확인할 것
  - VSCode - Python: Select Interpreter



<br>

### 2. Tokenizing

- 4월 11일
- `.noun_phrases`
  - Noun phrases를 한 번에 추출할 수 있는 TextBlob의 라이브러리를 사용함
  - 썸네일의 title과 content에 대해 추출을 진행한 결과
    - 내가 추출을 원하는 'nike x (브랜드명)'에서 x를 제거해버리는 문제가 발생
      - 파이썬의 find() 함수로 문제를 해결하기에는 해당 구문만을 추출할 수가 없음
    -  `' x '` 를 추출하고 앞 뒤의 공백을 제거하는 전처리 후, 명사구 추출을 계획함

<br>

- 정규표현식으로 문자열을 추출하고자 함
  - `re` 라이브러리를 import 하고, 검색할 패턴을 컴파일 해두는 방법으로 진행함
  - 매칭 메타 문자
    - `^x` : Start of Line-'x', 즉 문자열이 x로 시작함
    - `x$` : 'x'-End of Line, 즉 문자열이 x로 끝남
    - `.x` : any character-'x', 즉 임의의 한 문자를 표현함(x가 마지막으로 끝남)
  - `findall()`
    - 문자열에 패턴과 매칭되는 부분을 리스트로 전부 반환
    - 반환값이 리스트이기 때문에 group() 함수 등을 사용할 수 없음
  - `finditer()`
    - 오브젝트 형태로 된 이터레이터를 반환하기 때문에 for문 내에서 group() 함수를 사용 가능
    - 반환값이 오브젝트이기 때문에 인덱스로 접근 불가, len() 함수도 불가
  - `.span()`
    - 문자열 시작(start), 종료(end) 위치를 반환

<br>

- title에서 `' x '`를 추출한 결과
  - 썸네일의 개수와 matchObject의 개수가 맞지 않았음
  - 즉 title에  `' x '`를 중복하여 포함한 제목이 존재함을 확인함
  - 이를 확인하고 for문을 분리하여 문제를 해결함

<br>

- 4월 12일
- 어제의 정규표현식을 이용한 문자열 추출 작업이 삽질이었음을 깨달음
  - 추출한 `' x '` 에서 앞 뒤의 공백을 제거하기 위해서는 `replace()`를 쓰면 되었다
  - 허망하지만, 그래도 긍정적인 점은 어제의 작업을 통하여
    - 제목에 `' x '` 가 중복하여 있는 데이터가 있음을 알 수 있었던 것

<br>

- replace() 함수를 이용하여 `' x '` 를  `'-x-'` 로 치환 후 `in`을 이용하여
  - '(브랜드명)-x-(브랜드명)'을 포함한 데이터만을 추출함
  - 나아가 split() 함수를 이용하여 브랜드 명만을 추출함





<br>

### 3. ETL(Extract, Transform, Load)

- 4월 13일
- 썸네일과 body의 contents에 대해서도 브랜드명 추출 작업을 진행함
- 인덱스를 포함하여 추출한 데이터를 컬럼으로 관리할 필요성을 느낌 - pandas 이용
  - 추출한 데이터에 대한 인덱스별 중복 언급 여부를 확인하여 정리해야

<br>

- 4월 14일
- 첫번째 컬럼을 인덱스로 하여 데이터를 추출하도록 크롤러를 수정하고
- 코드를 통합하여 메인 크롤러로 정리함