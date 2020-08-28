import React, { useContext, useEffect } from 'react'
import NavbarComponent from './NavbarComponent'
import { Context } from '../context/Context'
import { Link } from 'react-router-dom'
import { apiUrl } from '../Globals'

export default function TemplatesComponent() {
    const data = useContext(Context)[0]

    useEffect(() => {
        console.log(data)
    }, [data])

    const mouseEntered = (id) => {
        document.getElementById(id).style.opacity = 1
    }

    const mouseLeft = (id) => {
        document.getElementById(id).style.opacity = 0
    }

    return (
        <div>
            <NavbarComponent />
            <div className="templates-container">
                <h1 className="header">Templates | {data.templates.length}</h1>
                <div className="templates">
                    {data.templates.map((d, i) => (
                        <div className="template" key={i}>
                            <img alt="" src={`${apiUrl}images/assets/${d.placeholderImage}`} />
                            <div className="underdog" id={`underdog${d.id}`} onMouseEnter={() => mouseEntered(`underdog${d.id}`)} onMouseLeave={() => mouseLeft(`underdog${d.id}`)}>
                                <Link className="btn" to={`/templates/${d.id}`}>
                                    USE
                                </Link>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}