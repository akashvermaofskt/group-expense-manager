export function PostData(type, userData){

    let BaseURL = 'http://127.0.0.1:8000/';

    return new Promise((resolve, reject) =>{
      console.log("Inside promise")
        console.log(JSON.stringify(userData))
        
        fetch(BaseURL+type, {
            method: 'POST',
            body: JSON.stringify(userData),
            headers: {
              "Content-Type": "application/json",
              "Accept": "*/*",
            },
          })
          .then((response) =>{ 
              resolve(response.json())
             console.log(response)
             
        })/*
          .then((res) => {
            resolve(res);
            //console.log(res)
          })*/
          .catch((error) => {
            reject(error);
          });

  
      });

}
