---
title: NodeJS password 저장과 static function
tags: ['nodejs']
categories: [☁️ NodeJS]
thumbnail: ''
permalink: ''
status: ''
date: 2021-10-04 22:08:20
---

mongoose 를 예시로, callback과 promise 함수를 알아본다.
`#hashing` `#login` `#bcrypt`
<!-- excerpt -->
<!-- toc -->

---

# Own static function

* hashtag 값을 저장할 때 Video.js(model)에 아래와 같이 save하기 전에 실행되는 middleware를 추가했었다.

```js
// save 이전의 middleaware
videoSchema.pre('save', async function (){
    this.hashtags = this.hashtags[0].split(",").map((word)=> (word.startwith("#")? word:`#${word}`));
});
```

<br>

* 하지만, save 이외의 query들은 pre middleware를 제공하지 않는다. 그렇기 때문에 따로 `static function` 을 만들어 사용할 수 있다.

> You cannot access the document being updated in pre('updateOne') or pre('findOneAndUpdate') query middleware. If you need to access the document that will be updated, you need to execute an explicit query for the document.

```js
videoSchema.static('formatHashtags', function (hashtags){
    return hashtags.split(",").map((word)=> (word.startsWith("#")? word:`#${word}`))
});
```

## regex 연산자(operator)
mongoose 의 연산자를 사용하여 원하는 검색결과를 얻을 수 있다.
우리가 사용한 연산자는 regex 이지만, 사이트에 더 많은 방법이 존재한다.


* RegExp: Search with Regular Expression

```js
export const search = async(req, res) => {
    // form 에 넘겨준 파라미터를 가지고 온다.
    const {keyword} = req.query;
    let videos= [];
    if(keyword){
        videos = await Video.find({
            title: {
                $regex: new RegExp(`${keyword}$`, "ig"),
            }
        });
    }
    return res.render("search", { pageTitle: "Search", videos });
};
```


---

# 비밀번호 저장: Hashing

## bcrypt (hash function)


* hash function: rainbow table 공격을 막아준다.
* hash 함수 중 하나인 `bcrypt` 함수를 이용하여 비밀번호를 DB에 저장 할것이다.
* hash는 `deterministic` 하기 때문에 동일한 input에 대해서 동일한 output을 갖는다.

👉🏼 [npmjs/bcrypt 공식사이트](https://www.npmjs.com/package/bcrypt)
공식 사이트에 아래와 같은 내용이 나와있다.

> To hash a password:
Technique 1 (generate a salt and hash on separate function calls):

* Technique 1

```js
bcrypt.genSalt(saltRounds, function(err, salt) {
    bcrypt.hash(myPlaintextPassword, salt, function(err, hash) {
        // Store hash in your password DB.
    });
});
```
* Technique 2 (auto-gen a salt and hash):
(saltRounds: 몇번 hash 할것인가?)

```js
bcrypt.hash(myPlaintextPassword, saltRounds, function(err, hash) {
    // Store hash in your password DB.
});
```

<br>

## Technique 2 (auto-gen a salt and hash) 사용

* User.js(model)에서 db에 저장되기 이전, 비밀번호 값에 hashing을 적용한다.

```js
userSchema.pre('save', async function(){
    // 비밀번호 hashing
    this.password = await bcrypt.hash(this.password, 5);
});
```

<br>

* 적용 전과 적용 후 db 조회시 비밀번호가 알수없는 hash값으로 저장된다는것을 확인할 수 있다.

```mongo
 db.users.find()
{ "_id" : ObjectId("615480ae204f405b9d35478a"), "email" : "suyans730@naver.com ", "username" : "sy", "password" : "1234", "name" : "Suyeon Kim", "__v" : 0 }
> db.users.find()
{ "_id" : ObjectId("615480ae204f405b9d35478a"), "email" : "suyans730@naver.com ", "username" : "sy", "password" : "1234", "name" : "Suyeon Kim", "__v" : 0 }
{ "_id" : ObjectId("6154853ff5a58157c6953ef3"), "email" : "aa@naver.com ", "username" : "ay", "password" : "$2b$05$EaF71tKmlQBcByXqFFLtBO6wADBkdC/AmlPOGSCbtZO44N8z5GO/u", "name" : "Amy", "__v" : 0 }
```

## 로그인에 적용하기

* hashing은 one-way이다. 즉, input에서 output은 가능하지만, output으로 input값을 다시 구할 수는 없다.
* 그래서 bcrypt는 compare를 제공한다. 이 함수를 사용하여 기존 비밀번호와 같은지 비교할 수 있다.

```js
bcrypt.compare(plaintextPassword, hash);
```