import React, {useState, createContext} from 'react';

export const Context = createContext();

export const Provider = (props) => {
    const [data, setData] = useState()
    return (
        <Context.Provider value={[data, setData]}>
            {props.children}
        </Context.Provider>
    )
}