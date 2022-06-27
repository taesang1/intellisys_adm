<template>
    <div style="height: 100%; border-right: 1px solid #eceeef; padding-left: 10px;">
        <li>
            <a>Service메뉴 관리</a>
            <ul>
                <li>
                    <a>조회</a>
                </li>
                <li>
                    <a>등록</a>
                </li>
            </ul>
        </li>
        <li>
            <a>Service 적용사례 관리</a>
            <ul>
                <li>
                    <a>조회</a>
                </li>
                <li>
                    <a>등록</a>
                </li>
            </ul>
        </li>
        <li>
            <a>문의하기 관리</a>
            <ul>
                <li>
                    <a>조회</a>
                </li>
                <li>
                    <a>폼 관리</a>
                </li>
            </ul>
        </li>
        <li>
            <a>blog 관리</a>
            <ul>
                <li>
                    <router-link style="text-decoration: none; color: black;" to="/blog_list">조회</router-link>
                </li>
                <li>
                    <router-link style="text-decoration: none; color: black;" to="/blog_write">작성</router-link>
                </li>
            </ul>
        </li>
    </div>
</template>
<style>
    li{
        font-size: 15px;
        padding: 5px 0px;
    }
    ul, li{
        list-style:none;
    }
</style>