# OAuth API

Illustrating the meticulous implementation of OAuth security measures within the configuration of an API endpoint, thereby exemplifying a comprehensive and robust framework designed to safeguard sensitive information and ensure secure access to the designated resources.

##### Request Headers
    Authorization
    Bearer <Generated Token>

## POST
  ##### Token Generation

```bash
http://localhost:8888/token
```

##### Body
    username    john
    password    password

Illustrates the systematic utilization of the POST method to generate a JWT (JSON Web Token), elucidating its pivotal role in facilitating secure authentication processes when interfacing with an API endpoint.


## POST
  ##### Post Creation

```bash
http://localhost:8888/root/postCreation
```
Illustrates the systematic application of a method designed for the creation of posts. Notably, the focus is on users who have undergone authentication through the utilization of a JWT token. This token, a pivotal component, is seamlessly incorporated in this process, showcasing its integral role in securing and authorizing the creation of posts within the designated framework.


## GET
  ##### Post Retrieval

```bash
http://localhost:8888/root/postRetrieval
```
Illustrates the structured approach of utilizing the method for posting data retrieval. The demonstration specifically underscores the crucial role of a JWT token, generated through a dedicated Token Generation method, emphasizing its validity period of one minute as a time-bound security measure when interacting with the relevant API endpoint.


## PUT
  ##### Post Update

```bash
http://localhost:8888/root/postUpdate
```
Illustrates the user-centric process of updating Post tiles. Users initiate the customization journey by setting preferences through a client-side interface. The backend system, employing a JWT token generated via a dedicated method, securely retrieves and processes data from the API endpoint based on these preferences. Emphasizing a one-minute validity period, the JWT token ensures a time-bound security measure. The result is a seamless and secure update of Post tiles, providing a personalized and engaging user experience.


## PUT
  ##### Post Hightlights Update

```bash
http://localhost:8888/root/postUpdate/<HighLightNumber>
```
Illustrates the customization of post highlights through a client-side interface, triggering a secure backend interaction. A JWT token, valid for one minute, authenticates the API endpoint access, ensuring a personalized and time-bound update to post highlights.


## DELETE
  ##### Post Delete

```bash
http://localhost:8888/root/postDelete/<PostID>
```
Illustrates the method for deleting a user-created post from the database, emphasizing the necessity of a JWT token for authentication. To execute the deletion, users must present a valid JWT token, ensuring a secure interaction with the database. This approach prioritizes both user authorization and data integrity, providing a robust and controlled method for post deletion.

#### Additional Resources
For more information on how the OAuth API works and the underlying REST principles, please refer to the following resources:

- [OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)
- [What Is a REST API? Examples, Uses, and Challenges](https://blog.postman.com/rest-api-examples/)
- [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

