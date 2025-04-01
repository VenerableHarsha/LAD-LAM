import { configureStore } from "@reduxjs/toolkit";
import messagesReducer from "./Messages";

const store = configureStore({
  reducer: {
    messages: messagesReducer,
  }, // Add reducers here when needed
});

export default store;
