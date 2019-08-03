import React from 'react';
import axios from 'axios';
import {Redirect} from "react-router-dom";

class Register extends React.Component {

  constructor(props) {
    super(props);
    this.state = { name:"", email: "", password: "",toLogin:false}; 
    this.onSubmit=this.onSubmit.bind(this);
    this.handleNameChange=this.handleNameChange.bind(this);
    this.handleEmailChange=this.handleEmailChange.bind(this);
    this.handlePasswordChange=this.handlePasswordChange.bind(this);
    this.register=this.register.bind(this);
  }

  register(userData){
    console.log(userData);
    let BaseURL = 'http://172.20.10.2:5000/api/';
    async function makePostRequest() {
        let res = await axios.post(BaseURL+'register/',userData);
        if(res.status==200){
          alert("An email verification link has been sent to your email address, Kindly verify withn 24 hours.");
        }else{
          alert(res.data);
        }
    }
    //makePostRequest();
    alert("User registered successfully! Please log in!");
    this.setState({
      toLogin:true
    });
  }

  onSubmit(e){
    e.preventDefault();
    let userData = { User: { Name: this.state.name , Email: this.state.email, Password: this.state.password}};
    this.register(userData);
  }
  handleNameChange(e){
    this.setState({ name: e.target.value });
  }
  handleEmailChange(e){
    this.setState({ email: e.target.value });
  }
  handlePasswordChange(e){
    this.setState({ password: e.target.value });
  }
  
  render() {

    if(this.state.toLogin===true){
      return <Redirect to="/" />
    }

    return (
      <div className="shadow-lg p-3 mb-5 bg-white rounded border border-dark">
          <h3>Register</h3>
          <form onSubmit={this.onSubmit}>
              <div className="form-group">
                  <input type="text" className="form-control" placeholder="Your Name *" onChange={this.handleNameChange}/>
              </div>
              <div className="form-group">
                  <input type="text" className="form-control" placeholder="Your Email *" onChange={this.handleEmailChange}/>
              </div>
              <div className="form-group">
                  <input type="password" className="form-control" placeholder="Your Password *"  onChange={this.handlePasswordChange}/>
              </div>
              <div className="form-group">
                  <input type="password" className="form-control" placeholder="Confirm Your Password *"  onChange={this.handlePasswordChange}/>
              </div>
              <div>
                <button type="submit" className="btn btn-primary">Register</button>
              </div>
          </form>
        </div>
    );
  }
}

export default Register;
  