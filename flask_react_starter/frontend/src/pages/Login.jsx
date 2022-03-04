import React, { Component } from 'react'
import { Link } from 'react-router-dom'

export default class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
           username:"",
           password:"" 
        }
        console.log(this,"inside constructor")
        this.handleChange = this.handleChange.bind(this)
        this.handleLogin = this.handleLogin.bind(this)
    
    }
    handleLogin(e){
        fetch('/api/login/', {
            method: 'POST', // or 'PUT'
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.state),
        })
            .then(response => response.json())
            .then(res => {
                if (res.error){
                    alert(res.message)
                }else{
                    window.localStorage.setItem("token",res.data.token)
                    window.localStorage.setItem("username", res.data.user.username)
                    window.localStorage.setItem("id", res.data.user._id.$oid)
                    window.location.href = "/"
                    alert(res.message)
                }
                console.log(res)
            })
            .catch((error) => {
                console.error('Error:', error);
            });

    }
    handleChange(e){
        this.setState({ ...this.state, [e.target.name]: e.target.value})
    }
    render() {
        return (
            <div>
                <div>
                    <label htmlFor="username">
                        Username {this.props.name} <br />
                        <input name="username" type="text" onChange={this.handleChange}/>
                    </label>
                </div>
                <div>
                    <label htmlFor="password"> Password <br />
                        <input name="password" type="password" onChange ={this.handleChange}/>
                    </label>
                </div>
                <br />
                <div>
                    <button onClick={this.handleLogin}> Login</button>
                </div>
                <Link to="/">Goto Home</Link><br />
                <Link to="/signup">Goto Signup</Link><br />
                <Link to="..">Go Back</Link>
            </div>
        )
    }
}
