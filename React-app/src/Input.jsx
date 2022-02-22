import React from "react";
const Input = ({ type, label, onchange }) => {

    return (
        <>
            <label>{label}</label>
            <input type={type} onChange={onchange} name={label} />
            <br />
        </>
    );
}

export default Input;