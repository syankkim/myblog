---
title: react router 사용하기
tags: ['Hooks','react','react router']
categories: [☁️ React]
img: <img width="100" alt="react-logo" src="https://user-images.githubusercontent.com/28856435/83209013-2c5fe280-a192-11ea-947e-18055da3d97e.png">
thumbnail: ''
permalink: ''
date: 2020-06-01 15:10:25
---

SPA 의 단점을 보완하고, 표준적으로 쓰이고 있는 `React Router` : `code split` 을 가능하게 해주는 라이브러리를 사용해 봅니다.
`React` `react router` `Hooks`
<!-- excerpt -->
<!-- toc -->


## React Router
> `React Router` 란, _SPA(Single Page Application: 모든코드를 하나의 파일에서 관리)_ 의 라우팅 문제를 보완할 수 있도록 코드의 모듈화를 가능하게 해주는 라이브러리 이다.
서로 다른 주소를 가진 view 를 만들어 관리한다. 즉, component 마다 다른 url 을 호출하여 화면을 그려줄 수 있다.
function 방식인 `Hooks` 를 적용.

---


예제에 대한 클래스 트리이다. 
&nbsp;&nbsp;&nbsp;public
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴindex.html
&nbsp;&nbsp;&nbsp;src
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ components
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ Header.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ Recipe.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ RecipeDetail.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ RecipeFind.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ RecipeNews.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ Chef.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ ChefDetail.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ App.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ index.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ server.js
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ㄴ package.json

<br/>

### App.js

* App.js 에서 Router 를 이용하여 각 함수들을 묶어준다.
```javascript
import React from 'react';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import logo from './logo.svg';
import './App.css';
import Header from "./components/Header";
import Recipe from "./components/Recipe";
import RecipeDetail from "./components/RecipeDetail";
import RecipeFind from "./components/RecipeFind";
import RecipeNews from "./components/RecipeNews";
import Chef from "./components/Chef";
import ChefDetail from "./components/ChefDetail";

/*
  index.js
  ReactDom.render(<App/>, document.getElementById('root'))
  <App/> => html 을 읽어서 => <div id="root"></div>
*/
function App() {
  return (
    <Router>
        <Header/>
        <div className={"container-fluid"}>
          <div className={"jumbotron"}>
            <Switch>
              <Route exact path={"/"} component={Recipe}/>
              <Route path={"/recipe_detail"} component={RecipeDetail}/>
              <Route path={"/chef"} component={Chef}/>
              <Route path={"/chef_detail"} component={ChefDetail}/>
              <Route path={"/news"} component={RecipeNews}/>
              <Route path={"/find"} component={RecipeFind}/>
            </Switch>
          </div>
        </div>

    </Router>
  );
}

export default App;
```

### Header.js
* navigation 을 그려주는 함수

```javascript
import React from "react";
import {NavLink} from "react-router-dom";

// <NavLink exact to={""}>
// NavLink 에서 exact 는 default 값이다.

//render()
export default function Header() {
    return (
        <nav className="navbar navbar-inverse">
            <div className="container-fluid">
                <div className="navbar-header">
                    <NavLink className="navbar-brand" to={"/"}>SIST Recipe</NavLink>
                </div>
                <ul className="nav navbar-nav">
                    <li className="active"><NavLink exact to={"/"}>레시피</NavLink></li>
                    <li><NavLink to={"/chef"}>쉐프</NavLink></li>
                    <li><NavLink to={"/news"}>레시피뉴스</NavLink></li>
                    <li><NavLink to={"/find"}>레시피검색</NavLink></li>
                </ul>
            </div>
        </nav>
    )
}
```

<br>

### Recipe.js
* App.js 에 넣어준 `RecipeDetail.js` `RecipeFind.js` ... 각 화면은 아래와 같이 `Recipe.js` 와 같은 함수 구조로 되어있다.
```javascript
import React from "react";

export default function Recipe() {
    return (
        <div><h1>레시피</h1></div>
    )
}
```

---
<br>

## server.js 서버를 생성하는 방법
>MongoDB 서버를 구축한다.
skip => offset 과 비슷하다.
* 라이브러리 로드
* 서버생성
* 서버구동
* cross domain 허용
* 클라이언트 통신 및 몽고디비 연결
* request 요청처리 => reponse 결과전송

```javascript
const express=require("express")
const app = express();

/*
* bind() => IP, PORT 를 연결 => 개통
* listen() => 대기상태
* accept() => 클라이언트가 접속시에 처리
* */
app.listen(3355, ()=>{
    console.log("Server Start ...", "http://localhost:3355")
})

// cross domain
app.all('/*', function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    next();
});

// 클라이언트 통신
// 사용자  URI => /recipe?page=1
// 몽고디비 연결
// MongoDB Connection
const Client = require("mongodb").MongoClient;
app.get('/recipe', (request, response)=>{
    // request => 사용자가 보낸 요청 : page, id, pwd
    // 요청 처리
    // response =>  결과전송
    var page= request.query.page; //request.getParameter("page")
    var rowSize =12;
    var skip = (page*rowSize) - rowSize;
    // 1page => skip=0
    // 2page => skip 12(버림) ==> 13

    var url = "mongodb://211.238.142.181:27017";
    Client.connect(url, (err, client)=>{
        var db = client.db('mydb');
        // SELECT * FROM recipe => find{()}
        // SELECT * FROM recipe WHERE no=1 => find{(no:1)}

        // skip => offset 과 비슷함.
        // toArray(err, docs) 콜백 함수: 가져온 데이터를 배열로 묶어줌. (docs에 있음)
        db.collection('recipe').find({}).skip(skip).limit(rowSize)
            .toArray((err, docs)=>{
                response.json(docs);
                client.close();
            });
    })

})
```
---

<br>

## axios: 서버에서 데이터 읽어오기

axios.get({`URL`, `params:{}`}).then((`result`)=>{ `setState변수(result.data)` })

![image](https://user-images.githubusercontent.com/28856435/83317751-f3933c80-a269-11ea-9cbc-43443ad22eeb.png)


* useState() 변수 `recipe` 데이터에 넣어준 값을 화면에 그려준다.

![image](https://user-images.githubusercontent.com/28856435/83318025-23dbda80-a26c-11ea-8897-fa78ec1e7771.png)

---
<br>

## NavLink: props 넘기기
>Recipe.js 내의 음식 이미지를 클릭하면 그 이미지에 해당하는 상세보기로 넘어갈 수 있도록 NavLink 를 달아줄 것이다.

_
* App.js
`RecipeDetail`의 path를 다음과 같이 바꿔준다. (no 변수가 추가됨)
`/recipe_detail` → `/recipe_detail/:no` 
```javascript
<Route path={"/recipe_detail/:no"} component={RecipeDetail}/>
```

* Recipe.js
`/recipe_detail/"+m.no`

```javascript
<NavLink to={"/recipe_detail/"+m.no}>
  <img src={m.poster} alt="Lights" style={{"width":"100%"}}/>
</NavLink>
```

* RecipeDetail.js
no 라는 파라미터를 `match` 를 사용하여 넘길 수 있다.
`props.match.params.no` 

방법1)
```javascript
export default function RecipeDetail(props) {
    return (
        <div><h1>레시피 상세보기: {props.match.params.no}</h1></div>
    )
}
```
방법2) `match`클래스를 props에 할당.
```javascript
export default function RecipeDetail(props) {
const {match} = props;
    return (
        <div><h1>레시피 상세보기: {match.params.no}</h1></div>
    )
}
```

* sever.js
사용자가 넘겨준 `no` 라는 파라미터는 서버단에서 `request.query.no` 로 받을 수 있다.
이 때, 형변환이 필요하다는 사실도 잊지 않는다.
즉, `/recipe-detail?no=1` 의 형식이다.
이제, `http://localhost:3355/recipe-detail` 를 사용할 수 있다.
```javascript
app.get('/recipe-detail', (request, response)=>{
    // 파라미터를 받는 방법
    var no = request.query.no;
    Client.connect(URL, (err, client)=>{
        var db = client.db('mydb');
        // 형변환 : Number() or parseInt()
        db.collection('recipe_detail').find({no:Number(no)}).toArray((err, docs)=>{
            response.json(docs[0]); // Array 타입이기 때문에 하나의 Object 만 가져온다.
            client.close();
        })
    });
})
```

* 다시 RecipeDetail.js
server.js 에서 만들었던 API 를 사용하여 상세정보를 뿌려준다.
```javascript
 const [detail, setDetail] = useState({});

 useEffect(()=>{
   axios.get('http://localhost:3355/recipe-detail', {
     params:{
       no: match.params.no
     }
   }).then((result)=>{
     setDetail(result.data);
   })
 },[])
```

