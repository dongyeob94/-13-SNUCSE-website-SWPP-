import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Row } from 'antd';

class AboutGreetings extends Component {
    render() {
        return (
            <div>
                <Row className="pageTitle">
                    <h3>학부장 인사말</h3>
                </Row>
                <div>
                
                </div>
                <div style={{ background: '#E8E8E8', padding: '30px' }}>
컴퓨터공학부는 30여 명의 훌륭한 교수진과 최신 시설을 갖추고 400여 명의 학부생과 300여 명의 대학원생에게 세계 최고 수준의 교육 연구 환경을 제공하고 있습니다. 멀티미디어 강의실, 전자도서관, 하드웨어-소프트웨어-프로젝트 실험실이 연중 개방되며 산학협동연구와 국책연구를 위한 별도의 컴퓨터연구소가 설치되어 있습니다.<br /><br />
컴퓨터공학부는 학문의 기초를 이루는 컴퓨터 구조 및 설계, 소프트웨어시스템, 네트워크, 컴퓨터 이론은 물론 모바일컴퓨팅, 멀티미디어, 컴퓨터게임, 그래픽스, 내장형 시스템, 바이오컴퓨팅, 유비쿼터스 컴퓨팅, 전자상거래, 암호 및 보안 등과 같은 새로운 분야를 선도적으로 개척해 나가고 있습니다. 또한 미국, 유럽, 일본, 아시아의 여러 대학과 협정을 수립하여 매년 다수의 학생-교수를 교류하고 있습니다. 컴퓨터공학부의 졸업생은 국내외 관련 산업계, 학계에 주로 진출하고 있으며 새로운 아이디어로 벤처 창업에 성공한 경우도 많습니다. 컴퓨터공학부의 교육은 강의, 실습, 프로젝트, 세미나, 협동연구와 같은 다양한 방법으로 진행되며 새로운 지식을 창조할 수 있는 미래의 지도자를 양성하는 데에 초점을 맞추고 있습니다.<br /><br />
저는 학부장으로 재임하는 동안 학문적 수월성(Academic Excellence), 최고의 교육(Better Education), 인접학문 및 산업과의 긴밀한 협동 (Collaboration)이라는 세 개의 목표(ABC)를 꾸준히 추구할 것입니다. 젊은 학부, 창의적인 학부, 긍지를 갖게 하는 학부라는 전통을 세울 것입니다.<br /><br />
컴퓨터공학부는 여러분들의 적극적인 지원과 참여를 기다리고 있습니다. 감사합니다.<br /><br />
                    <div className="flright">
                        <Link to={`/members`}>전화숙</Link>
                        <br />서울대학교 공과대학 컴퓨터공학부장
                    </div>
                </div>
            </div>
        )
    }
}

export default AboutGreetings;
