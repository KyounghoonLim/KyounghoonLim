import React from 'react'
import fabric from 'fabric'

export default function TextEditor() {
  // const canvas = new fabric.Canvas('editor')
  // const text = new fabric.Textbox('Hello world From Fabric JS', {
  //   width:250,
  //   cursorColor :"blue",
  //   top:10,
  //   left:10
  // });
  // canvas.add(text)
  return (
    <div>
      hi i'm canvas
      <canvas id='editor'>

      </canvas>
    </div>
  )
}
