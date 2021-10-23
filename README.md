# ko-wiki-api
[한국 위키피디아](https://ko.wikipedia.org/)의 아티클을 추출합니다.

## 1. Install
깃을 통해 설치를 진행합니다.
```bash
git clone https://github.com/Aiden-Jeon/ko-wiki-api
cd ko-wiki-api
pip install -e .
```
설치가 되면 버전을 확인합니다.
```bash
kowikiapi version
```
정상적으로 설치가 완료되면 다음과 같이 출력됩니다.
```bash
0.1
```


## 2. Article 추출
name argument를 통해 원하는 Article을 추출합니다.
```bash
kowikiapi extract --name="마블 엔터테인먼트" --save-dir results/
```

추출된 데이터는 `--save-dir` 을 통해 입력된 곳에 `{name}.txt`로 저장됩니다.  
위의 예시에서는 `마블 엔터테인먼트.txt`로 저장됩니다.   
`results/마블 엔터테인먼트.txt`를 확인하면 다음과 같습니다.
```bash
head -n 2 results/마블\ 엔터테인먼트.txt
```
```
마블 엔터테인먼트(영어: Marvel Entertainment, LLC)는 1998년 6월에 마블 엔터프라이즈와 토이 비즈의 합병으로 설립된 미국의 엔터테인먼트 회사이다. 월트 디즈니 컴퍼니의 자회사로 마블 코믹스의 만화책과 마블 시네마틱 유니버스의 영화를 제작하는 것으로 유명하다.
2009년 월트 디즈니 컴퍼니는 마블 엔터테인먼트를 40억 달러에 인수했으며, 이후 유한 책임 회사(LLC)가 되었다. 또한 마블 엔터테인먼트는 소니 픽처스 엔터테인먼트와 유니버설 스튜디오와의 영화 라이선스 계약을 맺었다.
```

## 3. 문장 분리 후 Article 추출
`-kss` 옵션을 이용해 문장이 분리된 Article을 추출 할 수 있습니다.  
`--line-length` 를 통해 주어진 값보다 character 수가 작은 문장은 추출하지 않고 넘어갈 수 있습니다.
default 값은 `10`입니다.
```bash
kowikiapi extract --name="마블 엔터테인먼트" --save-dir results/ --kss --line-length 10
```
 
추출된 `마블 엔터테인먼트.txt`의 내용은 다음과 같습니다.
```bash
head results/마블\ 엔터테인먼트.txt
```
```
마블 엔터테인먼트(영어: Marvel Entertainment, LLC)는 1998년 6월에 마블 엔터프라이즈와 토이 비즈의 합병으로 설립된 미국의 엔터테인먼트 회사이다.
월트 디즈니 컴퍼니의 자회사로 마블 코믹스의 만화책과 마블 시네마틱 유니버스의 영화를 제작하는 것으로 유명하다.
2009년 월트 디즈니 컴퍼니는 마블 엔터테인먼트를 40억 달러에 인수했으며, 이후 유한 책임 회사(LLC)가 되었다.
또한 마블 엔터테인먼트는 소니 픽처스 엔터테인먼트와 유니버설 스튜디오와의 영화 라이선스 계약을 맺었다.
마블 코믹스 원작의 영화 작품 목록
마블 시네마틱 유니버스
마블 익스피리언스(en:Marvel Experience) - 아시아 최초로 부산광역시에서 개최 예정
마블 엔터테인먼트 - 공식 웹사이트
마블 코리아 - 공식 카페
```
