import React, { useEffect} from 'react'
import TemplatesComponent from '../components/TemplatesComponent'
import '../styles/TemplatesStyle.css'

export default function TemplatesPage() {
    //CHANGE THE TITLE AND SET ACTIVE THE NAVBAR TAG
    useEffect(() => {
        document.title = 'GAMG | Templates'
        document.getElementById('templatesLinkNavbar').style.borderBottomColor = 'white'
        document.getElementById('templatesLinkNavbarMobile').style.borderLeftColor = 'white'
    }, [])

    return <TemplatesComponent />
}