import React, { useEffect } from 'react'
import TemplateComponent from '../components/TemplateComponent'
import '../styles/TemplateStyle.css'

export default function TemplatePage() {
    //CHANGE THE TITLE
    useEffect(() => {
        document.title = 'GAMG | Generator'
    }, [])

    return <TemplateComponent />   
}