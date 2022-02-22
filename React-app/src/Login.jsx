import React from "react";
import { useState } from "react";
import Input from "./Input";
import "./login.css";
const Login = (props) => {
    const [account, setAccount] = useState({ username: "", password: "" });
    const accountUpdate = (e) => {
        let val = e.target.value;
        let name = e.target.name;
        let copy = { ...account };
        copy[e.target.name] = val;
        setAccount(copy);



    }


    const submit = (e) => {
        e.preventDefault();

        console.log(account);

    }


    return (
        <div className="login">

            <form className="wrap" onSubmit={submit}>
                <h1>Login</h1>
                <Input type="text" label="username" onchange={accountUpdate} />
                <Input type="password" label="password" onchange={accountUpdate} />
                <button type="submit">Submit</button>


            </form>


        </div>


    );
}

export default Login;

