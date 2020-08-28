import React, { useEffect } from 'react'
import HomeComponent from '../components/HomeComponent'
import '../styles/HomeStyle.css'

export default function HomePage() {
    //CHANGE THE TITLE
    useEffect(() => {
        document.title = 'GAMG | HomePage'
    }, [])

    return <HomeComponent />
}