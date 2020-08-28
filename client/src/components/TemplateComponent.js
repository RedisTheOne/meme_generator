import React, { useEffect, useContext, useState } from 'react'
import NavbarComponent from './NavbarComponent'
import { useParams } from 'react-router-dom'
import { Context } from '../context/Context'
import { apiUrl } from '../Globals'
import Notification from './NotificationComponent'

export default function TemplateComponent() {
    const id = useParams().id
    const contextData = useContext(Context)[0]
    const [template, setTemplate] = useState({loading: true})
    const [imageUrl, setImageUrl] = useState("")
    const [copyMemeBtnDisplay, setCopyMemeBtnDisplay] = useState('none')
    const [copyMemeBtnTitle, setCopyMemeBtnTitle] = useState('COPY MEME URL')

    //Notification Props
    const xClicked = (title) => {
        setNotificationProps({title, right: -250, xClicked})
    }
    const [notificationProps, setNotificationProps] = useState({
        title: "",
        right: -250,
        xClicked
    })

    useEffect(() => {
        contextData.templates.forEach(c => {
            if(c.id === id)
                setTemplate({...c, loading: false})
        })
    }, [id, contextData])

    useEffect(() => {
        if(template.loading === false)
            setImageUrl(`${apiUrl}images/example/${template.example}`)
    }, [template])

    const generateClicked = () => {
        let isValid = true

        template.fields.forEach(t => {
            const value = document.getElementById(t.name).value
            
            if(t.type === "word") {
                if(value.includes(' '))
                    isValid = false
                
                if(value.length > 6 || value.length === 0)
                    isValid = false
            } else {
                const splitedValue = value.split(' ')
                if(!/\S/.test(value))
                    isValid = false

                if(splitedValue.length > 5)
                    isValid = false
                
                    splitedValue.forEach(v => {
                    if(v.length > 8)
                        isValid = false
                })
            }
        })

        if(isValid) {
            let body = `{"template": "${id}", `

            template.fields.forEach(t => {
                body += `"${t.name}": "${document.getElementById(t.name).value}",`
            })

            body = body.substring(0, body.length - 1)
            body += '}'

            setNotificationProps({title: 'Generating...', right: 10, xClicked})

            fetch(apiUrl + "generate", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body
            })
                .then(res => res.json())
                .then(data => {
                    setImageUrl(`${apiUrl}images/memes/${data.fileName}`)
                    setNotificationProps({title: 'Meme generated successfully', right: 10, xClicked})
                    setCopyMemeBtnDisplay('block')
                })

        } else 
            setNotificationProps({title: 'Filled fields are invalid', right: 10, xClicked})
    }

    const copyToClipboard = () => {
        setTimeout(() => setCopyMemeBtnTitle('COPY MEME URL'), 3000)
        // navigator.clipboard.writeText(imageUrl)
        //     .then(() => setCopyMemeBtnTitle('URL COPIED'))
        const input = document.getElementById('copyTextInput')
        input.value = imageUrl
        input.select()
        input.setSelectionRange(0, 99999)
        document.execCommand("copy")
        setCopyMemeBtnTitle('URL COPIED')
    }

    if(template.loading)
        return <div></div>

    return (
        <div>
            <NavbarComponent />
            <Notification
                props={notificationProps}
            />
            <div className="template-container">
                <div className="container-a">
                    <img alt="" src={imageUrl} />
                </div>
                <div className="container-b">
                    <div className="fields">
                        {template.fields.map((t, i) => (
                            <div key={i} className="field">
                                <label>{t.label}</label>
                                <input id={t.name} type="text" />
                            </div>
                        ))}
                    </div>
                    <div style={{display: 'flex'}}>
                        <button className="btn" onClick={() => generateClicked()}>GENERATE</button>
                        <button className="btn" style={{background: '#40916c', marginLeft: 10, display: copyMemeBtnDisplay}} onClick={() => copyToClipboard()}>{copyMemeBtnTitle}</button>
                    </div>
                    <input type="text" value="" style={{opacity: 0, outline: 0, cursor: 'default'}} id="copyTextInput" />
                </div>
            </div>
        </div>
    )
}