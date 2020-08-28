import React, { useState } from 'react'
import '../styles/NavbarStyle.css'
import { Link } from 'react-router-dom'

export default function NavbarComponent() {
    const [sidebarMarginLeft, setSidebarMarginLeft] = useState(-250)

    const optionsBtnClicked = () => {
        if(sidebarMarginLeft === -250)
            setSidebarMarginLeft(0)
        else
            setSidebarMarginLeft(-250)
    }


    return (
        <div className="navbar" style={{position: 'fixed'}}>
            <div className="left">
                <Link to={'/'}>
                    <h2 className="logo">GAMG</h2>
                </Link>
            </div>
            <div className="right desktop">
                <Link to={'/'} id="homeLinkNavbar">HOME</Link>
                <Link to={'/templates'} id="templatesLinkNavbar">TEMPLATES</Link>
            </div>
            <div className="right mobile">
                <i onClick={() => optionsBtnClicked()} className="fa fa-bars icon"></i>
            </div>
            <div className="sidebar" style={{marginLeft: sidebarMarginLeft}}>
                <h1>GAMG</h1>
                <div className="links">
                    <Link to={'/'}>HOME</Link>
                    <Link to={'/templates'} id="templatesLinkNavbarMobile">TEMPLATES</Link>
                </div>
            </div>
        </div>
    )
}