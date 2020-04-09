# Pjt_NIKE x











## Crawler





### 1. 모든 페이지의 썸네일에 대한 크롤링

- 4월 7일

- NIKE > Collaboration 페이지의 썸네일 내용
  - 즉 제목(title), 작성 일자(date), 간단한 내용(content)에 대한 크롤러를 구현함
- `Requests`, `BeautifulSoup`의 라이브러리를 활용하여, csv 파일로 데이터를 추출함
  - 개발자 도구의 `copy selector`를 이용
- 카테고리 내 페이지 모두를 크롤링하기 위해 `url의 패턴`을 찾음
  - 도메인 주소 뒤 /page/p(page number) 의 형태였기 때문에, 반복문을 활용함
- 페이지 수에 대한 반복문 내에 썸네일 수에 대한 반복문을 이중으로 작성하여
  - 모든 데이터를 딕셔너리 형태로 받음
- `with open`의 writer 권한으로 title, date, content를 필드 네임으로 하여 `DictWriter`로 csv 파일을 작성함
- 썸네일을 통한 본문 링크의 규칙 파악
  - 도메인 주소 뒤 제목을 소문자로 변환(lower()), 스페이스를 비롯한 기타 기호를 하이픈으로 변환(translate())의 규칙
  - 위의 규칙을 토대로 본문 내용 크롤링을 계획함





### 2. 모든 썸네일의 본문 링크에 대한 크롤링

- 4월 8일
- 전날 파악했던 본문 링크의 규칙이 하루만에 완전히 바뀌어버렸음을 확인함
  - 썸네일의 제목도, 요약도, 본문 중의 내용도 아닌 완전히 새로운 형태의 규칙이었음
  - 단 하루만에... 이것이 에자일인가요
  - 따라서 썸네일의 a 태그의 href를 크롤링하는 것으로 계획을 변경함

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

- 공식문서를 통해 a 태그 하나만을 가져오는 방법을 찾음

  - [calling-a-tag](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all)

  - `find_all()`

    > If you need to get all the <a> tags, or anything more complicated than the first tag with a certain name, you’ll need to use one of the methods described in [Searching the tree](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree), such as find_all():

  - `find()`와 `find_all()`의 용례를 파악하고 적용함

    - tag와 class명의 표기 방식에 유의할 것
    - data 객체를 스트링으로 변환했고
    - 큰따옴표의 인덱스로 슬라이싱하여 본문 링크를 추출할 수 있었음

    ```python
    a_href = []
    for i in range(1, 11):
        url = 'https://news.nike.com/collaborations/page/' + str(i)
    
        response = requests.get(url)
        response = response.text
        data = BeautifulSoup(response, 'html.parser')
    
        data = data.find('div', {'class':"col-md-10"})
        contents = data.find_all('div', {"class":"col-md-6 feature-tile__content"})
        
        for content in contents :
            a_tag_str = content.find_all('a')[1].__repr__()
            idx_start = 8
            idx_end = a_tag_str[9:].index('"')
            a_href.append([a_tag_str[9:idx_end+9]])
    ```

- data의 객체를 다루는 과정에서 라이브러리의 `__init__` 파일을 뜯어보기도 함

- VSCode의 Go Definition 기능도 유용하게 사용함
