import React from 'react'
import { Link } from 'react-router-dom'

export default function HomeComponent() {
    return (
        <div className="home-container">
            <h1>WELCOME TO GOOD ASS MEMES GENERATOR</h1>
            <Link to={'/templates'} className="btn">
                TEMPLATES
            </Link>
        </div>
    )
}