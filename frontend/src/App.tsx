import axios from 'axios';
import 'bootstrap'
import React, {useState, useEffect} from 'react'

function App() {

    const [getMessage, setGetMessage] = useState({});

    /* getting data from axios */
    useEffect(() => {
        axios.get('/profile')
            .then(res => {
                setGetMessage(res.data);
            }).catch(err => {
                console.log(err);
            }
        );
    }, []);

    const result = Object.keys(getMessage).map((key) => {
        return {[key]: getMessage[key as keyof typeof getMessage]};
    });

    return (
        <div className="App">
            {result.map((item: any, key: any) => {
                return (
                    <div key={key}>
                        <p className = {'text-danger'} >{item.name}</p>
                        <p>{item.about} </p>
                        <p>{item.dob}</p>
                    </div>
                )
            })}
        </div>
    );
}

export default App;
