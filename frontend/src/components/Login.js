import React from 'react';
import {Redirect} from 'react-router-dom';
class Login extends React.Component {

    constructor(props) {
      super(props);
      this.state = { email: "", password: ""}; 
      this.onSubmit=this.onSubmit.bind(this);
      this.handleEmailChange=this.handleEmailChange.bind(this);
      this.handlePasswordChange=this.handlePasswordChange.bind(this);
    }

    onSubmit(e){
      e.preventDefault();
      console.log(this.state);
      //POST REQUEST
      this.props.loginUser();
    }

    handleEmailChange(e){
      this.setState({ email: e.target.value });
    }
    handlePasswordChange(e){
      this.setState({ password: e.target.value });
    }
  
    render() {
      return (
        <div className="shadow-lg p-3 mb-5 bg-white rounded border border-dark">
          <h3>Login</h3>
          <form onSubmit={this.onSubmit}>
              <div className="form-group">
                  <input type="text"  className="form-control" placeholder="Your Email *" name="email" onChange={this.handleEmailChange}/>
              </div>
              <div className="form-group">
                  <input type="password" className="form-control" placeholder="Your Password *" name="password" onChange={this.handlePasswordChange}/>
              </div>
              <div>
                <button type="submit" className="btn btn-primary">Login</button>
              </div>
              <div >
                  <a href="#">Forget Password?</a>
              </div>
          </form>
        </div>
      );
    }
  
  }

  export default Login;