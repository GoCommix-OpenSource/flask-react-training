import React, { useState }  from 'react'


fetch(`/api/users/${window.localStorage.getItem("id")}/`, {
    method: 'get',
    headers: new Headers({
        'Authorization': 'Bearer ' + window.localStorage.getItem("token"),
        'Content-Type': 'application/json'
    })
})
.then(response => response.json())
.then(data => {
    setState(data.data)
})
.catch((error) => {
    console.error('Error:', error);
});
export default function GetUser() {
    const [state, setState] = useState({})
  return (
    <div>
        <p>
        </p>
        
    </div>
  )
}
