import { createSlice } from "@reduxjs/toolkit";

const messagesSlice = createSlice({
    name: "messages",
    initialState: {
        messages: [],
        first_send_check: false,
    },
    reducers: {
        addMessage: (state, action) => {
        state.messages.push(action.payload);
        },
        removeMessage: (state, action) => {
        state.messages = state.messages.filter(
            (message) => message.id !== action.payload.id
        );

        },
        setFirstSendCheck: (state) => {
            state.first_send_check = true;
        },
    },
});

export const { addMessage, removeMessage,setFirstSendCheck } = messagesSlice.actions;
export default messagesSlice.reducer;