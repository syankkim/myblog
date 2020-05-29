---
title: Hooks 로 함수형 코딩을 해보자
tags: ['Hooks','react']
categories: [☁️ React]
img: <img width="100" alt="react-logo" src="https://user-images.githubusercontent.com/28856435/83209013-2c5fe280-a192-11ea-947e-18055da3d97e.png">
thumbnail: ''
permalink: ''
date: 2020-05-29 09:38:23
---

클래스에서 사용했던 기능을 함수에서도 사용할 수 있도록 해주는 HOOKS 를 사용해봅니다.
`useState` `useEffect` `useMemo`, `useCallBack`
<!-- excerpt -->
<!-- toc -->

---

# Hooks ?
> 클래스에서 사용했던 기능을 함수에서도 사용할 수 있도록 해줌.

## useState
>  const [변수명, 메소드]= useState("[]")

* EX
```javascript
const [music, setMusic] = useState([]);
```

## useEffect

>React의 class  방식의 componentDidMount 생명주기를 흉내낼 수 있다.
useEffect(fn, [])

* 클래스 방식
```javascript
componentDidMount(){
    this.setstate({music:})
 }
```
* 함수 방식 : `useState` 에서 정의해주었던 `music` 변수를 저장하고 있는 `setMusic` state를 사용.
```javascript
useEffect(() => {
        axios.get("http://localhost:3000/music.json")
            .then((res) => {   // res에 데이터 불러옴
                setMusic(res.data);
                console.log(res.data);
            })
    },[]);

```

* 그런데 `[]` 는 뭔가요? deps 란?
>mount 할때마다 실행. => componentDidMount, componentDidUpdate
시작하자마자 한번만 읽어로려면, 즉 didMount 에만 함수를 적용하고 싶다면,
함수의 2번째 인자로 `[] deps` 를 줘야함.
내용 갱신 시에는 deps 를 쓰지 않는다.

---

* 잠깐 문법
```javascript
// 이렇게 하면 forEach 가능한데
props.music.forEach((m)=>{
         ...   
    })

// html 에서 스크립트를 만들 때는 forEach 적용이 안됨.
const html = music.map((m)=>
        <tr>
            <td>{m.rank}</td>
        </tr>
)
```


---

### 검색 이벤트 등록

* 사용 함수
 AppMain() : main 함수이다.
 SearchBar()
 MusicTable()

* `handleUserInput` 라는 이벤트 등록함수를 만들어 준다.
* 이렇게 이벤트를 넘겨주는 방식은 `callByReference` 방식이다.
callByReference 는 주소값을 넘겨준다. javaScript 는 pointer 로 이루어져 있어 주소값으로 넘겨준다면 이 값은 변할 수 있다.
* 변수 str 을 넘겨주는 방식은 `callByValue` 방식이다.
복사라고 생각하면 된다. 가지고 있는 걸 사용하는 것이 아닌, 새로 똑같은 값을 만들어준다.

__AppMain()__
```javascript
function App3() {
	// 변수 설정
    const [music, setMusic] = useState([]);
    // 변수 초기값
    const [str, setStr]= useState("");

    useEffect(()=>{
        axios.get("http://localhost:3000/music.json")
            .then((res)=>{
                setMusic(res.data);
            })
    },[])  // mount 할때마다 실행. => componentDidMount, componentDidUpdate

    // 이벤트 등록
    const handleUserInput= (str)=>{
        setStr(str);
    }
     return(
        <div className={"row"}>
            <H/>
            <SearchBar str={str} onUserInput={handleUserInput}/>
            <div style={{"height":"30px"}}></div>
            <MusicTable music={music} str={str}/>
        </div>
    )
}
    
```

* `onUserInput` 이벤트를 연결한다. 이벤트가 발생한 곳의 값(input 태그의 값)을 가져와 `onUserInput`에 값을 넣어준다.
__SearchBar(str)__
```javascript

function SearchBar(props) {
    // useCallBack
    const onChange=(e)=>{
        props.onUserInput(e.target.value);
    }

    return(
        <table className={"table"}>
            <tr>
                <td>
                    <input type={"text"} size={"25"} className={"input-sm"}
                        placeholder={"search"} onChange={onChange} value={props.str}/>
                </td>
            </tr>
        </table>
    )
}
```

## CallBack : useCallBack()
> * hooks 의 기능중 `useCallBack()` 함수를 사용한다. :함수의 주소를 기억하고 있다. Paging 에서 많이 사용된다.
Memory 누수가 안됨.
* 2번 째 인자로 deps :[str] 을 준다. : 검색내용이 변경 될 때에만 함수가 `handleUserInput` 호출되도록 변경해준다.
```javascript
  const handleUserInput= useCallback((str)=>{
    setStr(str);
  }, [str]) // str 이 변경될 때에만 호출된다.
```


* 실제로 데이터를 출력해주는 함수
__MusicTable()__
```javascript
function MusicTable(props) {
    let row=[];
    props.music.forEach((m)=>{
        if(m.title.indexOf(props.str)==-1){
            return;
        }
        // 배열에 추가
        row.push(<MusicRow music={m}/>);
    })

    return(
        <table className={"table"}>
            <thead>
                <tr className={"danger"}>
                    <th>순위</th>
                    <th></th>
                    <th>노래명</th>
                    <th>가수</th>
                </tr>
            </thead>
            <tbody>
            {row}
            </tbody>
        </table>
    )
}
```

## React.memo
> * React 는 컴포넌트를 렌더링 한 뒤, 이전 렌더링 된 결과와 비교하여 DOM 업데이트를 결정한다. 이전 렌더링 결과와 비교하는 과정은 충분히 빠르지만 이 과정에서 속도를 줄일 수 있다.
* `React.memo` 로 매핑될 때, React 는 컴퍼넌트를 렌더링 후 그 결과를 `메모이징(Memoizing)` 한다. 그 다음 렌더링 시 `props` 가 같다면 메모이징 했던 내용을 재사용한다.
[출처] https://ui.toast.com/weekly-pick/ko_20190731/

* 위에서 진행했던 예제로 계속 설명을 한다면,
* SearchBar 에  입력할 때마다 즉, `onUserInput` 이벤트가 발생할 때마다  `MusicTable` 을 재렌더링 한다.
그 때마다 H1 태그는 글자 색상을 랜덤으로 가져온다. `Math.random()*5`
* 즉, input 창에 뭔가를 적을 때마다 반짝반짝 하며 타이틀 색상이 수시로 바뀌게 되는 ...뭔가 고쳐주고 싶은 현상을 발견한다.
* 이 때 사용하는것이 바로 `memo`

* React.memo 적용전
```javascript
const H=()=>{
    // memo : 호출한것 기억.
    const color = ['red','blue','green','yellow','pink'];
    const no = parseInt(Math.random()*5);
   // 배열 인덱스 5개중 랜덤수 선택
    return(
        <h1 className={"text-center"} style={{"color":color[no]}}>Music Top 50</h1>
    )
}
```
* React.memo 적용 후: searchBar 에 입력해도 변하지 않음.
```javascript
const H=React.memo(()=>{
    // memo : 호출한것 기억.
    const color = ['red','blue','green','yellow','pink'];
    const no = parseInt(Math.random()*5);
   // 배열 인덱스 5개중 랜덤수 선택
    return(
        <h1 className={"text-center"} style={{"color":color[no]}}>Music Top 50</h1>
    )
})
```