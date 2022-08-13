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
            <div className="flex flex-col bg-white border rounded-sm w-100 hover:border-blue-600 hover:border-2">
                <div className="p-4">
                    <div className="flex items-center justify-between">
                        <div className="flex">
                            <div
                                style="background: #2f80ed"
                                className="flex items-center justify-center w-12 h-12 rounded-full">
                            </div>
                            <div className="ml-2">
                                <h2 style="color: #576f7f" className="text-lg font-semibold">
                                    hhhh
                                </h2>
                                <em style="color: #576f7f" className="text-sm">
                                    <div
                                        v-for="(item, myIndex) in developer_type.slice(0, 1)"
                                        className="card-tags-dev">
                                    </div>
                                </em>
                            </div>
                        </div>
                        <div>
                            <em style="color: #576f7f" className="text-sm"></em>
                        </div>
                    </div>
                    <div className="h-{100px} pt-3">
                        <p
                            style="color: #576f7f; margin-right: 0.5rem py-2"
                            className="text-base font-normal before:content-['>>']"
                        >
                            Favourite Languages
                        </p>
                        <div className="pt-2 card-tags">
                            <div className="h-{20px}">
                                <span className="hover:bg-blue-500">jjj</span>
                            </div>
                        </div>
                    </div>
                    <div className="h-{100px} pt-3">
                        <p
                            style="color: #576f7f; margin-right: 0.5rem"
                            className="text-base font-normal before:content-['>>']"
                        >
                            Favourite Frameworks
                        </p>
                        <div className="py-2 card-tags">
                            <div>
                                <span className="hover:bg-blue-500"></span>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="height: 1px; background: #d8d8d8" className="w-full"/>
                <div style="background: #f7f7f7" className="p-2">
                </div>
            </div>
            {result.map((item: any, key: any) => {
                return (
                    <div key={key}>
                        <p className={'text-danger'}>{item.name}</p>
                        <p>{item.about} </p>
                        <p>{item.dob}</p>
                    </div>
                )
            })}
        </div>
    );
}

export default App;
