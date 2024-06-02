import { useState } from "react"
import { GrUpload } from "react-icons/gr";
import { MdDeleteOutline } from "react-icons/md";
import "../../css/IdentifyFood/UploadImage.css";

export const UploadImage = () => {
    const [image, setImage] = useState(null);
    return (
        <div className="upload-container">
            {image && (
                <div className="remove-image">
                    <MdDeleteOutline/>
                </div>
            )}
            <div className="upload">
                <GrUpload size={"40px"}/>
                <p>Click to Upload</p>
            </div>
        </div>
    )
}