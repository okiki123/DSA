//JSX (Javascript XML)

export default function App() {
    return (
        <div>
            <h1>Welcome to React!</h1>
        </div>
    )
}

export default function Greetings ({ message }) {
    return (<h1>{`Hello ${message}`}</h1>)
}

// React State 

import React, { useState } from "react";
import ReactDOM from "react-dom";
function User() {
    const [message, setMessage] = useState('Welcome to react');

    return (
        <div>
            <h1>{message}</h1>
        </div>
    )
}

const ChildComponent = (props) => {
    return (
        <div>
            <p>{props.name}</p>
            <p>{props.age}</p>
        </div>
    )
}

const ParentComponent = () => {
    return (
        <div>
            <ChildComponent name = "Okiki" age = "25" />
            <ChildComponent name = "Malomo" age = "27" />
            <button onClick={activateLasers}></button>
        </div>
    )
}

setState({ name: "Daniel" }, () => {
    console.log("The name has been updated ")
})