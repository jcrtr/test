import {useState} from "react";

export function Timer() {
    let [time, setTime] = useState();

    useState(() =>{
        setTime = new Date().toLocaleString()
    })

    return (
        <>
            {time}
        </>
    )
}