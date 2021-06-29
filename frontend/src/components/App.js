import React, { Component, component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";


// takes component and renders in the app and displays on the page
export default class App extends Component {
    constructor(props) {
        super(props);
        // this.state = {} whenever this edited will rerender our components
    }
    
    render() {
        return (
            <div>
                <HomePage />
            </div>
        ); // can pass props into home page now
    }
}
// to embed JS code into html text, use {}
// e.g. {this.props.name}

const appDiv = document.getElementById("app");

// can pass props into app
render(<App />, appDiv)