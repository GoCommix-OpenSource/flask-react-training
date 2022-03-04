import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';

export default class Signup extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: ""
        }
        this.signupFunction = this.signupFunction.bind(this)
        this.handleChange = this.handleChange.bind(this)
    }
    signupFunction(e) {
        console.log(this.state)
        fetch('/api/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.state)
        })
            .then(function (response) {
                return response.json()
            }).then(function (body) {
                console.log(body);
            });
    }
    handleChange(e) {
        this.setState({ ...this.state, [e.target.name]: e.target.value.trim() })
    }
    render() {
        return (
            <Fragment>
                <form method="post" id="signupForm" > {/*action="/api/user/"*/}
                    <div>
                        <input type="text" name="username" placeholder="username" onChange={this.handleChange} />
                    </div>
                    <div>
                        <input type="password" name="password" placeholder="password" onChange={this.handleChange} />
                    </div>
                    <div>
                        <input type="button" value="Submit" onClick={this.signupFunction} />
                    </div>
                </form>
                <Link to="/">Goto Home</Link><br/>
                <Link to="/login">Goto Login</Link><br />
                <Link to="..">Go Back</Link>
            </Fragment>
        )
    }
}
