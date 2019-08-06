import React from 'react';
import {BrowserRouter as Router,Route,Link} from "react-router-dom";
import ReactMultiSelectCheckboxes from 'react-multiselect-checkboxes';

class CreateGroup extends React.Component{
    constructor(props){
        super(props);
        this.state={
            groupname:"",

        }
        this.onSubmit=this.onSubmit.bind(this);
    }
    options = [
        { label: 'Friend 1', value: 1},
        { label: 'Friend 2', value: 2},
      ];
    onSubmit(e){
        e.preventDefault();
        this.props.history.push("/");
    }
    render(){
        return (
        <Router>
            <div className="container">
                <div>
                    <h1 className="text-center font-weight-bold">Create Group</h1>
                </div>
                <div id="main" className="container-fluid mt-5" style={{background:"white",color:"black"}}>
                <div className="shadow-lg p-3 mb-5 bg-white rounded border border-dark">
                <h3>Create Group</h3>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <input type="text" className="form-control" placeholder="Group Name *"/>
                    </div> 
                    <div>
                        <button type="submit" className="btn btn-primary" >Create</button>
                    </div>
                </form>
                </div>
                </div>
            </div>
        </Router>
        
        );
    }
}

export default CreateGroup;
